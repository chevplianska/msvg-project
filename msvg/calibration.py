"""Model calibration to market option prices."""

import numpy as np
from scipy.optimize import minimize

from .markov_chain import markov_vg_cf
from .option_pricing import fft_call_price
from .vg_process import VGParams, vg_cf


def calibrate_single_vg(market_strikes, market_prices, T, r, S0, initial_params=None, bounds=None):
    """Calibrate single VG model to market option prices."""
    if initial_params is None:
        initial_params = [0.2, 0.1, 0.0]
    if bounds is None:
        bounds = [(0.01, 1.0), (0.01, 1.0), (-1.0, 0.0)]

    def objective(params):
        sigma, nu, theta = params
        if sigma <= 0 or nu <= 0:
            return 1e10
        vg_fit = VGParams(sigma, nu, theta)
        prices_fit = fft_call_price(market_strikes, T, r, S0, lambda u: vg_cf(u, T, vg_fit))
        return np.sum((prices_fit - market_prices) ** 2)

    res = minimize(objective, initial_params, method="L-BFGS-B", bounds=bounds)
    return VGParams(res.x[0], res.x[1], res.x[2])


def calibrate_markov_vg(market_strikes, market_prices, T, r, S0, initial_params=None, bounds=None):
    """Calibrate Markov VG model to market option prices."""
    if initial_params is None:
        initial_params = [0.2, 0.1, 0.0, 0.3, 0.2, -0.2, 1.0, 2.0, 0.7]
    if bounds is None:
        bounds = [(0.01, 1.0), (0.01, 1.0), (-1.0, 0.0)] * 2 + [
            (0.1, 10.0),
            (0.1, 10.0),
            (0.1, 0.9),
        ]

    def objective(params):
        sigma0, nu0, theta0, sigma1, nu1, theta1, lam01, lam10, p0 = params
        if (
            sigma0 <= 0
            or nu0 <= 0
            or sigma1 <= 0
            or nu1 <= 0
            or lam01 <= 0
            or lam10 <= 0
            or p0 < 0
            or p0 > 1
        ):
            return 1e10
        try:
            vg0_fit = VGParams(sigma0, nu0, theta0)
            vg1_fit = VGParams(sigma1, nu1, theta1)
            cf_fit = lambda u: markov_vg_cf(u, T, vg0_fit, vg1_fit, lam01, lam10, p0)
            prices_fit = fft_call_price(market_strikes, T, r, S0, cf_fit)
            if np.any(np.isnan(prices_fit)) or np.any(np.isinf(prices_fit)):
                return 1e10
            error = np.sum((prices_fit - market_prices) ** 2)
            if np.isnan(error) or np.isinf(error):
                return 1e10
            return error
        except:
            return 1e10

    res = minimize(objective, initial_params, method="L-BFGS-B", bounds=bounds)

    fit_vg0 = VGParams(res.x[0], res.x[1], res.x[2])
    fit_vg1 = VGParams(res.x[3], res.x[4], res.x[5])
    fit_lam01, fit_lam10, fit_p0 = res.x[6], res.x[7], res.x[8]

    return fit_vg0, fit_vg1, fit_lam01, fit_lam10, fit_p0
