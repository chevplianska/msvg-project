"""FFT-based option pricing (Carr-Madan), PDF recovery, and implied vol."""

import numpy as np
from py_lets_be_rational import implied_volatility_from_a_transformed_rational_guess
from py_lets_be_rational.exceptions import AboveMaximumException, BelowIntrinsicException


def fft_call_price(strikes: np.ndarray[float], T, r, S0, cf_xt_func):
    """Price European call options using FFT (Carr-Madan method)."""
    strikes = np.asarray(strikes, dtype=float)
    k_range = np.log(strikes / S0)

    N = 4096
    alpha = 1.5
    eta = 0.25
    lamb = 2.0 * np.pi / (N * eta)

    v = np.arange(N) * eta
    k_fft = -0.5 * N * lamb + np.arange(N) * lamb

    phi_minus_i = cf_xt_func(np.array([-1j]))[0]
    compensator = np.log(phi_minus_i)
    drift = r * T - compensator

    def cf_log_moneyness(u):
        return np.exp(1j * u * drift) * cf_xt_func(u)

    u_eval = v - (alpha + 1.0) * 1j
    denom = alpha**2 + alpha - v**2 + 1j * (2.0 * alpha + 1.0) * v
    numer = np.exp(-r * T) * cf_log_moneyness(u_eval)

    psi = np.zeros(N, dtype=complex)
    mask = np.abs(denom) > 1e-12
    psi[mask] = numer[mask] / denom[mask]

    weights = np.ones(N) * (2.0 / 3.0) * eta
    weights[0] = (1.0 / 3.0) * eta
    weights[-1] = (1.0 / 3.0) * eta
    weights[1::2] = (4.0 / 3.0) * eta

    fft_input = np.exp(1j * v * (0.5 * N * lamb)) * psi * weights
    fft_out = np.fft.fft(fft_input)

    price_norm = np.exp(-alpha * k_fft) * np.real(fft_out) / np.pi

    prices_interp = np.interp(k_range, k_fft, price_norm)
    return S0 * prices_interp


def pdf_from_cf(x_range, cf_xt_func, damping=0.001, u_max=50.0, n_nodes=4096):
    """Recover PDF via numerical integration of the characteristic function.

    ``u_max`` must be large enough that the characteristic function has decayed:
    a density of width ``s`` needs roughly ``u_max * s >> 1``. The defaults suit
    the order-one log-return scales of the paper replication. For sharply peaked
    densities -- short maturities, or a large ``nu`` after time rescaling --
    raise ``u_max`` (and ``n_nodes`` with it, to keep the oscillatory integrand
    resolved), or rescale to ``tau = 1`` first with ``msvg.scale_to_unit_time``.
    """
    x_range = np.asarray(x_range, dtype=float)
    N = int(n_nodes)
    u = np.linspace(0, float(u_max), N)

    cf_vals = cf_xt_func(u)
    cf_vals = np.where(np.isfinite(cf_vals), cf_vals, 0.0)

    x_col = x_range[:, np.newaxis]
    integrand = np.real(np.exp(-1j * u * x_col) * cf_vals * np.exp(-damping * u))
    # NumPy 2.x renamed ``trapz`` to ``trapezoid`` and NumPy 2.4 removed the
    # legacy alias. Keep the paper implementation usable on both NumPy 1.x and
    # 2.x without forcing an environment downgrade.
    trapezoid = getattr(np, "trapezoid", None)
    if trapezoid is None:  # NumPy < 2.0
        trapezoid = np.trapz
    pdf = trapezoid(integrand, u, axis=1) / np.pi

    return np.maximum(pdf, 0.0)


def _call_put_q(flag, shape):
    values = np.broadcast_to(np.asarray(flag), shape).reshape(-1)
    out = np.empty(values.size, float)
    for i, value in enumerate(values):
        token = str(value).lower()
        if token in {"c", "call"}:
            out[i] = 1.0
        elif token in {"p", "put"}:
            out[i] = -1.0
        else:
            raise ValueError("flag must be 'c' or 'p'")
    return out.reshape(shape)


def _jaeckel_iv(undiscounted_price, forward, strike, maturity, q_flag):
    if not (
        np.isfinite(undiscounted_price)
        and np.isfinite(forward)
        and np.isfinite(strike)
        and np.isfinite(maturity)
        and forward > 0.0
        and strike > 0.0
        and maturity > 0.0
    ):
        return np.nan
    try:
        sigma = implied_volatility_from_a_transformed_rational_guess(
            float(undiscounted_price),
            float(forward),
            float(strike),
            float(maturity),
            float(q_flag),
        )
    except (BelowIntrinsicException, AboveMaximumException):
        return np.nan
    if not np.isfinite(sigma) or sigma <= 0.0:
        return np.nan
    return float(sigma)


def implied_vol(price, S, K, T, r, flag="c", q=0.0):
    """Black–Scholes–Merton implied vol via Jäckel's Let's Be Rational.

    ``flag`` is ``'c'``/``'p'`` (scalar or per-quote). ``q`` is the continuous
    dividend yield. Invalid quotes (below intrinsic, above the forward bound)
    return NaN.
    """
    price, spot, strike, maturity, rate, yield_ = np.broadcast_arrays(
        np.asarray(price, float),
        np.asarray(S, float),
        np.asarray(K, float),
        np.asarray(T, float),
        np.asarray(r, float),
        np.asarray(q, float),
    )
    q_flag = _call_put_q(flag, price.shape)
    discount = np.exp(-rate * maturity)
    forward = spot * np.exp((rate - yield_) * maturity)
    undiscounted = price / discount
    sigma = np.empty(price.shape, float)
    for idx in np.ndindex(price.shape):
        sigma[idx] = _jaeckel_iv(
            undiscounted[idx],
            forward[idx],
            strike[idx],
            maturity[idx],
            q_flag[idx],
        )
    return sigma if sigma.ndim else float(sigma)
