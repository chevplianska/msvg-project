"""Option-chain preprocessing and BBO-aware calibration.

Implements the pipeline of ``notebooks/option_chain_calibration_protocol.md``:

    BBO quotes -> put-call parity carry (D, A, F) -> synthetic-call surface
                -> implied-volatility band -> IV band loss -> VG / MSVG fit

Everything downstream of the carry fit consumes ``(D, F)`` only, so no carry
term is ever applied twice and no volatility parameter is asked to compensate
for a mislocated forward.
"""

import numpy as np
import pandas as pd
from scipy.optimize import LinearConstraint, differential_evolution, linprog, minimize

from .markov_chain import markov_vg_cf
from .option_pricing import fft_call_price, implied_vol, pdf_from_cf
from .vg_process import VGParams, vg_cf

YEAR_SECONDS = 365.25 * 24 * 3600

# --- IV band conventions (Section 11) -------------------------------------
EPS_VOL = 0.005   # floor on the IV band width, in vol points
#: Smallest out-of-the-money premium, relative to the largest on the chain, that
#: a strike must carry to be scored. Screens the near-intrinsic tail in the
#: market's own units, including the one-sided strikes ``MAX_IV_WIDTH`` cannot
#: see. See :func:`build_iv_band`.
MIN_OTM_PREMIUM = 1e-3
MAX_IV_WIDTH = 0.10   # discard two-sided bands wider than this: the market is
                      # not pinning vol there, so the strike carries no
                      # volatility information and only adds inversion noise.


# --------------------------------------------------------------------------
# Snapshot loading and call/put pairing
# --------------------------------------------------------------------------
def load_snapshot(path):
    """Load a parquet chain snapshot; return (quotes, observation timestamp)."""
    raw = pd.read_parquet(path)
    raw["timestamp"] = pd.to_datetime(raw["timestamp"])
    raw["right"] = raw["right"].astype(str).str.lower()
    stamp = raw["timestamp"].max()
    return raw.loc[raw["timestamp"].eq(stamp)].copy(), stamp


def year_fraction(observed, expiry):
    """Time to maturity in years, using the actual settlement timestamp."""
    return (expiry - observed).total_seconds() / YEAR_SECONDS


def pair_call_put(snapshot):
    """Join calls and puts by strike and form the parity bands.

    Returns one row per strike with the parity difference band
    ``[lower_bound, upper_bound]`` implied by the quoted BBO:

        C - P in [C_bid - P_ask,  C_ask - P_bid].
    """
    calls = snapshot.loc[snapshot["right"].eq("call")].set_index("strike")
    puts = snapshot.loc[snapshot["right"].eq("put")].set_index("strike")
    joined = (
        calls[["bid", "ask"]].rename(columns={"bid": "call_bid", "ask": "call_ask"})
        .join(
            puts[["bid", "ask"]].rename(columns={"bid": "put_bid", "ask": "put_ask"}),
            how="inner",
        )
        .dropna()
    )
    healthy = (
        (joined["call_ask"] >= joined["call_bid"])
        & (joined["put_ask"] >= joined["put_bid"])
        & (joined["call_ask"] > 0)
        & (joined["put_ask"] > 0)
    )
    joined = joined.loc[healthy]
    joined["lower_bound"] = joined["call_bid"] - joined["put_ask"]
    joined["upper_bound"] = joined["call_ask"] - joined["put_bid"]
    return joined.reset_index().sort_values("strike").reset_index(drop=True)


# --------------------------------------------------------------------------
# Carry: the two-variable linear feasibility problem in (A, D)
# --------------------------------------------------------------------------
def estimate_carry(pairs):
    """Recover the discount factor and forward from all strikes simultaneously.

    Every strike contributes ``lower_i <= A - D*K_i <= upper_i``. That is a
    two-variable linear feasibility problem, solved once over all ``2n``
    inequalities rather than by enumerating strike pairs.

    Feasibility is established first (is the chain internally consistent?), then
    a representative pair is selected inside the feasible set by a band-width
    weighted least-squares fit to the parity-band midpoints. If the exact set is
    empty the fallback minimizes total squared band violation, and
    ``exact_feasible`` reports that fact rather than hiding it.
    """
    cols = pairs[["strike", "lower_bound", "upper_bound"]].dropna().astype(float)
    strikes, lower, upper = (cols[c].to_numpy() for c in cols.columns)
    if len(strikes) < 2 or np.any(lower > upper):
        raise ValueError("need >=2 strikes with lower_bound <= upper_bound")

    pivot = strikes.mean()                       # centre for conditioning
    design = np.column_stack((np.ones_like(strikes), -(strikes - pivot)))
    stacked = np.vstack((design, -design))
    rhs = np.r_[upper, -lower]
    bounds = [(None, None), (np.finfo(float).eps, 1.0)]

    feasible = linprog([0.0, 0.0], A_ub=stacked, b_ub=rhs, bounds=bounds, method="highs")

    width = upper - lower
    scale = max(1.0, np.max(np.abs(np.r_[lower, upper])))
    weight = 1.0 / np.maximum(width, np.finfo(float).eps * scale) ** 2
    target = (lower + upper) / 2

    if feasible.success:
        loss = lambda x: np.sum(weight * (design @ x - target) ** 2)
        grad = lambda x: 2 * design.T @ (weight * (design @ x - target))
        fit = minimize(
            loss, feasible.x, jac=grad, bounds=bounds,
            constraints=LinearConstraint(design, lower, upper), method="SLSQP",
            options={"ftol": 1e-12, "maxiter": 1000},
        )
        low = linprog([0.0, 1.0], A_ub=stacked, b_ub=rhs, bounds=bounds, method="highs")
        high = linprog([0.0, -1.0], A_ub=stacked, b_ub=rhs, bounds=bounds, method="highs")
        d_min = float(low.x[1]) if low.success else np.nan
        d_max = float(high.x[1]) if high.success else np.nan
    else:
        start = np.linalg.lstsq(design, target, rcond=None)[0]

        def loss(x):
            gap = design @ x
            slack = np.minimum(gap - lower, 0) + np.maximum(gap - upper, 0)
            return float(slack @ slack)

        def grad(x):
            gap = design @ x
            slack = np.minimum(gap - lower, 0) + np.maximum(gap - upper, 0)
            return 2 * design.T @ slack

        fit = minimize(loss, start, jac=grad, bounds=bounds, method="L-BFGS-B")
        d_min = d_max = np.nan

    intercept, discount = fit.x
    prepaid = intercept + discount * pivot
    parity = design @ fit.x
    violated = int(np.sum((parity < lower - 1e-9) | (parity > upper + 1e-9)))
    return {
        "D_hat": float(discount),
        "A_hat": float(prepaid),
        "F_hat": float(prepaid / discount),
        "D_min": d_min,
        "D_max": d_max,
        "exact_feasible": bool(feasible.success),
        "objective": float(loss(fit.x)),
        "n_strikes": int(len(strikes)),
        "n_violated": violated,
    }


def implied_rate(discount, tau):
    """Continuously compounded rate implied by a discount factor."""
    return -np.log(discount) / tau


# --------------------------------------------------------------------------
# Synthetic-call surface
# --------------------------------------------------------------------------
def build_call_surface(pairs, D_hat, A_hat):
    """Present one call-price object to the call-only FFT pricer.

    Keeps the liquid out-of-the-money side at every strike: quoted calls for
    ``K >= F``, and quoted puts converted through parity for ``K < F`` using
    ``C = P + A - D*K``. The originating side is retained as metadata.
    """
    forward = A_hat / D_hat
    strikes = pairs["strike"].to_numpy(float)
    use_call = strikes >= forward
    bid = np.where(use_call, pairs["call_bid"], pairs["put_bid"] + A_hat - D_hat * strikes)
    ask = np.where(use_call, pairs["call_ask"], pairs["put_ask"] + A_hat - D_hat * strikes)
    surface = pd.DataFrame({
        "strike": strikes,
        "bid": bid,
        "ask": ask,
        "source": np.where(use_call, "C", "P"),
        "moneyness": strikes / forward,
    })
    surface["mid"] = (surface["bid"] + surface["ask"]) / 2
    healthy = (surface["ask"] > 0) & (surface["ask"] >= surface["bid"])
    return surface.loc[healthy].reset_index(drop=True)


# --------------------------------------------------------------------------
# Implied-volatility band (Section 11)
# --------------------------------------------------------------------------
def price_to_iv(price, strikes, tau, r, A_hat):
    """Invert call prices with the same carry the pricer uses.

    Passing the prepaid forward ``A`` as spot with rate ``r`` makes the
    Black-Scholes forward ``A*exp(r*tau) = F``, i.e. the parity forward, so the
    inversion and the pricer share one carry convention exactly.

    Deep in-the-money strikes cannot be rescued by nudging the price back onto
    the intrinsic floor, and it is worth knowing why. At ``K/F = 0.412`` on the
    2026-08-10 chain, intrinsic exactly returns no implied volatility, intrinsic
    plus one hundredth of a cent returns 79%, and plus one cent returns 114%.
    The map from price to volatility is numerically dead there -- the market's
    own 2.5 cents of time value invert to 125%. Any snapping tolerance would
    manufacture a volatility out of the tolerance itself. Such strikes must be
    excluded, which :func:`build_iv_band` does on band width, not rescued.
    """
    return implied_vol(price, A_hat, strikes, tau, r, flag="c", q=0.0)


def build_iv_band(surface, tau, r, A_hat, max_width=MAX_IV_WIDTH,
                  min_premium=MIN_OTM_PREMIUM):
    """Invert the synthetic-call BBO into an implied-volatility band.

    A zero bid admits any volatility down to zero, so no lower bound exists;
    those strikes are marked ``one_sided`` and are penalized only from above.
    Strikes whose ask does not invert, or whose two-sided band is wider than
    ``max_width``, are dropped as carrying no volatility information.

    That width test has a hole, and it is the one that matters: a one-sided
    strike *has* no width, so the test cannot see it at all. Deep in the money
    that is exactly the dangerous case -- the option is worth thousands of
    dollars of intrinsic value, "any volatility down to zero is consistent" is
    vacuously true, and the surviving one-sided constraint is unbounded in loss
    terms. On 2026-08-12 a single K/F = 0.387 quote of this kind accounted for
    94% of the objective.

    ``min_premium`` closes the hole in the market's own units. The
    out-of-the-money premium ``min(C, P)/A`` is defined for every strike
    regardless of the bid, and it decays to nothing on both wings, so it screens
    precisely the strikes the width test is blind to. The two agree wherever
    both apply: on 2026-08-10 every strike the width test drops is also dropped
    here, and the survivors span K/F 0.669-1.184 with no moneyness constant
    anywhere in the calibration.

    The alternative -- inverting those strikes anyway -- does not work, and
    :func:`price_to_iv` documents why: the price-to-volatility map is
    numerically dead that deep in the money.
    """
    strikes = surface["strike"].to_numpy(float)
    bid = surface["bid"].to_numpy(float)
    ask = surface["ask"].to_numpy(float)

    sigma_ask = price_to_iv(ask, strikes, tau, r, A_hat)
    sigma_bid = np.where(
        bid > 1e-8, price_to_iv(np.maximum(bid, 1e-12), strikes, tau, r, A_hat), np.nan
    )

    invertible = np.isfinite(sigma_ask) & (sigma_ask > 0)
    band = surface.loc[invertible].copy()
    band["sigma_bid"] = sigma_bid[invertible]
    band["sigma_ask"] = sigma_ask[invertible]
    band["one_sided"] = ~np.isfinite(band["sigma_bid"].to_numpy())

    two_sided = ~band["one_sided"].to_numpy()
    width = np.where(
        two_sided, band["sigma_ask"].to_numpy() - band["sigma_bid"].to_numpy(), np.nan
    )
    band["iv_width"] = width
    forward = A_hat * np.exp(r * tau)
    band_K = band["strike"].to_numpy(float)
    # Out-of-the-money premium min(C, P), normalized by the prepaid forward. The
    # put is recovered by the same parity relation that built the surface, so no
    # new carry assumption enters.
    call_mid = band["mid"].to_numpy(float)
    put_mid = call_mid - A_hat + np.exp(-r * tau) * band_K
    premium = np.where(band_K >= forward, call_mid, put_mid) / A_hat
    band["otm_premium"] = premium
    informative = band["one_sided"].to_numpy() | (width <= max_width)
    liquid = premium >= min_premium * np.max(premium)
    return band.loc[informative & liquid].reset_index(drop=True)


#: Penalty charged for a model price that admits no implied volatility.
#: Must exceed any loss a genuine fit could incur, otherwise the optimizer can
#: *buy* it: driving every price out of the no-arbitrage range would cap the
#: loss at a constant and beat an honest fit. See ``UNINVERTIBLE_PENALTY``.
UNINVERTIBLE_PENALTY = 1e4


def iv_band_loss(sigma_model, sigma_bid, sigma_ask, eps_vol=EPS_VOL, otm_premium=None):
    """Zero inside the IV band; squared vol distance outside, per band width.

    Vega collapses in both wings, so a price-space band loss makes wing misfit
    nearly free while over-weighting near-intrinsic strikes. Implied volatility
    is the unit in which strikes are comparable, and normalizing by the band
    width holds tightly quoted strikes to a tighter standard.

    ``sigma_bid`` NaN marks a one-sided (zero-bid) strike, penalized only from
    above. ``sigma_model`` NaN marks a model price outside the no-arbitrage
    range; it is charged ``UNINVERTIBLE_PENALTY`` rather than a small constant,
    because a cheap constant is an arbitrage *in the objective itself*.

    ``otm_premium`` supplies the out-of-the-money premium ``min(C, P)`` per
    strike, weighting each squared residual by it. The band width alone does not
    control the wings: a zero-bid strike is one-sided *by construction* and so
    bypasses the width filter entirely, which is how a single K/F = 0.387 quote
    came to account for 94% of the objective on 2026-08-12. The premium decays
    to nothing on both wings -- that strike carries 3.9e-04 of the at-the-money
    weight -- so it suppresses uninformative strikes smoothly, in the units the
    market actually trades, rather than through a moneyness cutoff whose
    location is a free parameter.
    """
    two_sided = np.isfinite(sigma_bid)
    width = np.maximum(np.where(two_sided, sigma_ask - sigma_bid, eps_vol), eps_vol)
    above = np.maximum(sigma_model - sigma_ask, 0.0) / width
    below = np.where(two_sided, np.maximum(sigma_bid - sigma_model, 0.0) / width, 0.0)
    loss = np.where(np.isfinite(sigma_model), above**2 + below**2, UNINVERTIBLE_PENALTY)
    if otm_premium is not None:
        # Weight the penalty too, not just the residual. Charging an
        # unweighted constant makes the uninvertible case *immune* to the
        # weighting, which inverts the intent exactly where it matters: a
        # deep-ITM strike whose model price misses the intrinsic floor by a
        # cent has no implied volatility, and would otherwise collect the full
        # penalty despite carrying 4e-04 of the at-the-money weight.
        premium = np.asarray(otm_premium, float)
        loss = loss * (premium / max(float(np.max(premium)), 1e-300))
    return loss


def arbitrage_violation(prices, strikes, D_hat, A_hat):
    """Fraction of model prices outside the static no-arbitrage call range.

    A European call must satisfy ``(A - D*K)^+ <= C <= A``. Model prices that
    breach this are not merely mispriced, they are not option prices at all.
    """
    prices = np.asarray(prices, float)
    lower = np.maximum(A_hat - D_hat * np.asarray(strikes, float), 0.0)
    bad = ~np.isfinite(prices) | (prices < lower - 1e-8) | (prices > A_hat + 1e-8)
    return float(np.mean(bad))


def band_premium(band):
    """OTM-premium weights for a band, or ``None`` if the column is absent."""
    return band["otm_premium"].to_numpy(float) if "otm_premium" in band else None


def score_surface(sigma_model, band, prices_model=None):
    """Report the IV band criterion plus familiar price-space diagnostics."""
    sigma_bid = band["sigma_bid"].to_numpy()
    sigma_ask = band["sigma_ask"].to_numpy()
    loss = iv_band_loss(sigma_model, sigma_bid, sigma_ask, otm_premium=band_premium(band))
    inside = np.where(
        np.isfinite(sigma_bid),
        (sigma_model >= sigma_bid) & (sigma_model <= sigma_ask),
        sigma_model <= sigma_ask,
    )
    report = {
        "iv_band_loss": float(np.mean(loss)),
        "frac_inside": float(np.mean(inside)),
        "n": int(len(loss)),
        "n_one_sided": int(band["one_sided"].sum()),
    }
    if prices_model is not None:
        bid, ask = band["bid"].to_numpy(), band["ask"].to_numpy()
        report["mid_price_rmse"] = float(np.sqrt(np.mean((prices_model - (bid + ask) / 2) ** 2)))
        report["frac_inside_price"] = float(np.mean((prices_model >= bid) & (prices_model <= ask)))
    return report


# --------------------------------------------------------------------------
# Model pricing and calibration
# --------------------------------------------------------------------------
def price_vg(params, strikes, tau, r, A_hat):
    """European calls under single-state VG, located on the parity forward."""
    sigma, nu, theta = params
    return fft_call_price(strikes, tau, r, A_hat, lambda u: vg_cf(u, tau, VGParams(sigma, nu, theta)))


def price_msvg(params, strikes, tau, r, A_hat):
    """European calls under two-state Markov-switching VG."""
    s0, n0, t0, s1, n1, t1, lam01, lam10, p0 = params
    cf = lambda u: markov_vg_cf(
        u, tau, VGParams(s0, n0, t0), VGParams(s1, n1, t1), lam01, lam10, p0
    )
    return fft_call_price(strikes, tau, r, A_hat, cf)


PRICERS = {"vg": price_vg, "msvg": price_msvg}

VG_BOUNDS = [(0.02, 1.2), (0.005, 3.0), (-2.0, 0.5)]
MSVG_BOUNDS = VG_BOUNDS * 2 + [(0.05, 20.0), (0.05, 20.0), (0.02, 0.98)]
BOUNDS = {"vg": VG_BOUNDS, "msvg": MSVG_BOUNDS}


def calibration_objective(kind, params, strikes, tau, r, A_hat, sigma_bid, sigma_ask,
                          D_hat=None, otm_premium=None):
    """Mean IV band loss. Identical for VG and MSVG by construction.

    Model prices are first required to be genuine call prices: finite and inside
    ``[(A - D*K)^+, A]``. Degenerate corners of the MSVG characteristic function
    can emit prices of order ``1e28`` (or negative), which invert to no implied
    volatility at all; without this guard the optimizer can drive *every* strike
    out of the invertible range and collect a constant penalty that undercuts an
    honest fit.
    """
    try:
        prices = PRICERS[kind](params, strikes, tau, r, A_hat)
        if not np.all(np.isfinite(prices)):
            return 1e12
        discount = D_hat if D_hat is not None else np.exp(-r * tau)
        lower = np.maximum(A_hat - discount * np.asarray(strikes, float), 0.0)
        # Carr-Madan interpolates in log-moneyness, so deep-ITM prices carry a
        # small absolute error against the intrinsic floor. Tolerate that, but
        # not a genuine breach: the tolerance is relative to the prepaid forward.
        tol = 1e-4 * A_hat
        if np.any(prices < lower - tol) or np.any(prices > A_hat + tol):
            # Scale the penalty with the size of the breach so the optimizer is
            # pushed back toward the admissible set rather than wandering on a
            # flat plateau.
            breach = (np.maximum(lower - prices, 0.0) + np.maximum(prices - A_hat, 0.0)).max()
            return 1e12 + float(np.log1p(breach))
        sigma_model = price_to_iv(prices, strikes, tau, r, A_hat)
        return float(np.mean(iv_band_loss(sigma_model, sigma_bid, sigma_ask,
                                          otm_premium=otm_premium)))
    except Exception:
        return 1e12


def calibrate(kind, band, tau, r, A_hat, seed=42, maxiter=200, popsize=18):
    """Fit ``kind`` in {'vg', 'msvg'} to an IV band.

    The loss is multi-modal in the MSVG parameters, so a global search runs
    first and a local polish follows. Both models receive the same surface,
    the same loss, and the same optimizer treatment.
    """
    strikes = band["strike"].to_numpy(float)
    sigma_bid = band["sigma_bid"].to_numpy(float)
    sigma_ask = band["sigma_ask"].to_numpy(float)
    discount = np.exp(-r * tau)
    premium = band_premium(band)
    target = lambda p: calibration_objective(
        kind, p, strikes, tau, r, A_hat, sigma_bid, sigma_ask,
        D_hat=discount, otm_premium=premium,
    )

    globally = differential_evolution(
        target, BOUNDS[kind], seed=seed, maxiter=maxiter, popsize=popsize,
        tol=1e-12, polish=True, init="sobol",
    )
    # The polish MUST carry the bounds. Without them Nelder-Mead walks out of
    # the admissible set: on 2026-08-11 it reached lambda_01 = -12.3, a negative
    # switching intensity, which is not a probability model at all. The loss
    # does not notice, because the characteristic function still evaluates.
    locally = minimize(
        target, globally.x, method="Nelder-Mead", bounds=BOUNDS[kind],
        options={"maxiter": 8000, "maxfev": 8000, "xatol": 1e-10, "fatol": 1e-14},
    )
    best, loss = ((locally.x, locally.fun) if locally.fun < globally.fun
                  else (globally.x, globally.fun))
    best = np.asarray(best, float)
    return {
        "kind": kind,
        "params": best,
        "loss": float(loss),
        "success": bool(globally.success),
        "n_iter": int(globally.nit),
        "admissible": check_admissible(kind, best),
    }


def check_admissible(kind, params):
    """Structural checks the box constraints cannot express.

    A finite loss is not evidence that the parameters mean anything: the
    characteristic function evaluates happily at a negative switching
    intensity, so the objective never notices that the generator has stopped
    being a generator. These are the conditions that make the fit a model.
    """
    params = np.asarray(params, float)
    report = {}
    states = [params[:3]] if kind == "vg" else [params[:3], params[3:6]]
    # E[e^{X_T}] < inf: the strip of regularity must contain Im(u) = -1.
    report["martingale_margin"] = [
        float(1.0 - theta * nu - 0.5 * sigma**2 * nu) for sigma, nu, theta in states
    ]
    report["martingale_ok"] = all(m > 0 for m in report["martingale_margin"])
    report["positive_vol"] = all(s > 0 and n > 0 for s, n, _ in states)
    if kind == "msvg":
        lam01, lam10, p0 = params[6], params[7], params[8]
        report["rates_positive"] = bool(lam01 > 0 and lam10 > 0)
        report["p0_is_probability"] = bool(0.0 <= p0 <= 1.0)
        report["stationary_p0"] = float(lam10 / (lam01 + lam10)) if lam01 + lam10 > 0 else float("nan")
    report["ok"] = all(v for k, v in report.items() if isinstance(v, bool))
    return report


def evaluate(kind, params, band, tau, r, A_hat, level=1.0):
    """Score fixed parameters against a (possibly later) IV band.

    ``level`` rescales the variance clock only (see ``price_at_level``), leaving
    every shape parameter frozen.
    """
    strikes = band["strike"].to_numpy(float)
    prices = price_at_level(kind, params, strikes, tau, r, A_hat, level)
    sigma_model = price_to_iv(prices, strikes, tau, r, A_hat)
    return score_surface(sigma_model, band, prices_model=prices), prices, sigma_model


# --------------------------------------------------------------------------
# Level / shape decomposition
# --------------------------------------------------------------------------
def price_at_level(kind, params, strikes, tau, r, A_hat, level=1.0):
    """Price with the variance clock rescaled by ``level``, shape frozen.

    The process is run to ``level * tau`` while the option is still inverted at
    the true ``tau``, so total variance scales by ``level`` and the implied
    volatility level moves roughly as ``sqrt(level)``. Every shape parameter --
    skew, kurtosis, both regimes, both switching intensities -- is untouched.

    This is the Lévy analogue of an SSVI level factor: it isolates the "parallel
    shift" of the volatility surface from its shape. The carry is held fixed by
    compensating the rate so the forward stays ``A * exp(r * tau) = F``.
    """
    if level == 1.0:
        return PRICERS[kind](params, strikes, tau, r, A_hat)
    tau_eff = float(level) * tau
    r_eff = r * tau / tau_eff            # keep A * exp(r_eff * tau_eff) = F
    return PRICERS[kind](params, strikes, tau_eff, r_eff, A_hat)


def fit_level(kind, params, band, tau, r, A_hat, bracket=(0.05, 40.0), tol=1e-4):
    """Refit only the variance level to a later band, holding shape frozen.

    Answers a specific question: how much of a frozen model's out-of-sample
    decay is a stale volatility *level*, and how much is the *shape* no longer
    describing the market? Refitting one scalar per day is not a
    non-anticipating forecast, and results using it must be labelled as a
    diagnostic rather than as an out-of-sample score.
    """
    from scipy.optimize import minimize_scalar

    strikes = band["strike"].to_numpy(float)
    sigma_bid = band["sigma_bid"].to_numpy(float)
    sigma_ask = band["sigma_ask"].to_numpy(float)

    def objective(log_level):
        prices = price_at_level(kind, params, strikes, tau, r, A_hat, np.exp(log_level))
        if not np.all(np.isfinite(prices)):
            return 1e12
        sigma_model = price_to_iv(prices, strikes, tau, r, A_hat)
        return float(np.mean(iv_band_loss(sigma_model, sigma_bid, sigma_ask)))

    result = minimize_scalar(
        objective, bounds=(np.log(bracket[0]), np.log(bracket[1])),
        method="bounded", options={"xatol": tol},
    )
    return float(np.exp(result.x)), float(result.fun)


def atm_iv(kind, params, tau, r, A_hat, level=1.0, width=0.15, n=161):
    """Model at-the-money implied volatility, interpolated at ``K = F``."""
    forward = A_hat * np.exp(r * tau)
    grid = forward * np.linspace(1 - width, 1 + width, n)
    prices = price_at_level(kind, params, grid, tau, r, A_hat, level)
    sigma = price_to_iv(prices, grid, tau, r, A_hat)
    good = np.isfinite(sigma)
    return float(np.interp(forward, grid[good], sigma[good]))


def prepare_snapshot(path, expiry):
    """Full preprocessing chain for one ``(underlying, expiry, timestamp)``."""
    snapshot, stamp = load_snapshot(path)
    pairs = pair_call_put(snapshot)
    carry = estimate_carry(pairs)
    tau = year_fraction(stamp, expiry)
    rate = implied_rate(carry["D_hat"], tau)
    surface = build_call_surface(pairs, carry["D_hat"], carry["A_hat"])
    band = build_iv_band(surface, tau, rate, carry["A_hat"])
    return {
        "timestamp": stamp,
        "spot": float(snapshot["underlying_price"].iloc[0]),
        "pairs": pairs,
        "carry": carry,
        "tau": tau,
        "r": rate,
        "A_hat": carry["A_hat"],
        "F_hat": carry["F_hat"],
        "D_hat": carry["D_hat"],
        "surface": surface,
        "band": band,
    }


# --------------------------------------------------------------------------
# Risk-neutral densities
# --------------------------------------------------------------------------
def scale_to_unit_time(kind, params, tau):
    """Rescale parameters so the law of ``X_tau`` is read off at ``tau = 1``.

    The VG characteristic exponent is homogeneous in a way that lets the whole
    maturity be absorbed into the parameters:

        X_tau  =d=  sqrt(tau) * Y_1,
        Y_1 ~ VG(sigma, nu / tau, sqrt(tau) * theta),

    which holds exactly (verified to ~1e-16 against ``vg_cf``). For the
    switching model each state rescales the same way and the intensities, being
    rates per unit time, become ``lambda * tau``.

    This matters numerically. A 14-day density has a standard deviation of a few
    percent, and recovering it directly by Fourier inversion needs a very large
    ``u_max``; at ``tau = 1`` the same law is order-one wide and inverts
    comfortably. Returns ``(scaled_params, scale)`` where the density maps back
    as ``p_X(x) = p_Y(x / scale) / scale``.
    """
    scale = np.sqrt(tau)
    if kind == "vg":
        sigma, nu, theta = params
        return [sigma, nu / tau, scale * theta], scale
    s0, n0, t0, s1, n1, t1, lam01, lam10, p0 = params
    return [s0, n0 / tau, scale * t0,
            s1, n1 / tau, scale * t1,
            lam01 * tau, lam10 * tau, p0], scale


def _unit_time_cf(kind, scaled):
    if kind == "vg":
        return lambda u: vg_cf(u, 1.0, VGParams(*scaled))
    s0, n0, t0, s1, n1, t1, lam01, lam10, p0 = scaled
    return lambda u: markov_vg_cf(
        u, 1.0, VGParams(s0, n0, t0), VGParams(s1, n1, t1), lam01, lam10, p0
    )


def risk_neutral_density(kind, params, tau, x=None, level=1.0,
                         u_max=4000.0, n_nodes=32768, n_points=1200):
    """Risk-neutral density of the martingale-adjusted log return ``X_tau``.

    Evaluated at ``tau = 1`` via ``scale_to_unit_time`` and mapped back, which
    keeps the Fourier inversion well conditioned at short maturities. ``level``
    applies the same variance rescaling as ``price_at_level``.

    Returns ``(x, density)``. The density integrates to one up to quadrature
    error, which is the property that makes it a fair diagnostic: unlike implied
    volatility, a density cannot hide a level error, because the mass is
    constrained.
    """
    scaled, scale = scale_to_unit_time(kind, params, float(level) * tau)
    cf = _unit_time_cf(kind, scaled)
    compensator = float(np.real(np.log(cf(np.array([-1j]))[0])))

    if x is None:
        # Width from the rescaled variance: at tau = 1 the VG variance is
        # sigma^2 + theta^2 * nu per state, so six standard deviations is a
        # generous window in every case encountered here.
        if kind == "vg":
            sigma, nu, theta = scaled
            var = sigma**2 + theta**2 * nu
        else:
            s0, n0, t0, s1, n1, t1, _, _, _ = scaled
            var = max(s0**2 + t0**2 * n0, s1**2 + t1**2 * n1)
        half = max(6.0 * float(np.sqrt(var)), 0.5)
        y = np.linspace(-half, half, n_points)
    else:
        y = np.asarray(x, float) / scale

    density_y = pdf_from_cf(y + compensator, cf, u_max=u_max, n_nodes=n_nodes)
    return y * scale, density_y / scale


def market_density_bl(band, tau, r, A_hat, smooth=0.0):
    """Breeden-Litzenberger density implied by the quoted midpoint surface.

    ``p(K) = exp(r * tau) * d^2 C / dK^2`` on the call-equivalent midpoints,
    converted to the density of the martingale-adjusted log return so it is
    directly comparable with :func:`risk_neutral_density`.
    """
    strikes = band["strike"].to_numpy(float)
    mid = ((band["bid"] + band["ask"]) / 2).to_numpy(float)
    order = np.argsort(strikes)
    strikes, mid = strikes[order], mid[order]

    second = np.gradient(np.gradient(mid, strikes), strikes)
    density_k = np.exp(r * tau) * second

    forward = A_hat * np.exp(r * tau)
    x = np.log(strikes / forward)
    density_x = np.maximum(density_k, 0.0) * strikes   # dK = S dx
    return x, density_x
