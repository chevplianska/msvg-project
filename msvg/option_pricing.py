"""FFT-based option pricing (Carr-Madan) and PDF recovery."""

import numpy as np


def fft_call_price(strikes, T, r, S0, cf_xt_func):
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


def pdf_from_cf(x_range, cf_xt_func, damping=0.001):
    """Recover PDF via numerical integration of the characteristic function."""
    x_range = np.asarray(x_range, dtype=float)
    N = 4096
    u_max = 50.0
    u = np.linspace(0, u_max, N)

    cf_vals = cf_xt_func(u)
    cf_vals = np.where(np.isfinite(cf_vals), cf_vals, 0.0)

    x_col = x_range[:, np.newaxis]
    integrand = np.real(np.exp(-1j * u * x_col) * cf_vals * np.exp(-damping * u))
    pdf = np.trapz(integrand, u, axis=1) / np.pi

    return np.maximum(pdf, 0.0)
