"""Monte Carlo simulation utilities."""

import numpy as np

from .markov_chain import _markov_mc_kernel, markov_vg_cf
from .vg_process import _vg_increment, vg_cf


def monte_carlo_single_vg(T, r, S0, vg, n_sims=100_000):
    """Monte Carlo simulation for single VG model."""
    X_T = _vg_increment(T, vg.sigma, vg.nu, vg.theta, size=n_sims)

    cf_val = vg_cf(np.array([-1j]), T, vg)[0]
    analytic_mean_X = np.real(cf_val)

    S_T = S0 * np.exp(r * T) * np.exp(X_T) / analytic_mean_X
    return S_T


def monte_carlo_markov_vg_numba(
    T, r, S0, vg0, vg1, lam01, lam10, p0, n_sims=100_000, n_steps=500, seed=42
):
    """Monte Carlo simulation for Markov-switching VG model."""
    dt = T / n_steps

    X_T = _markov_mc_kernel(
        n_sims,
        n_steps,
        dt,
        lam01,
        lam10,
        vg0.sigma,
        vg0.nu,
        vg0.theta,
        vg1.sigma,
        vg1.nu,
        vg1.theta,
        p0,
        seed,
    )

    cf_val = markov_vg_cf(np.array([-1j]), T, vg0, vg1, lam01, lam10, p0)[0]
    analytic_mean_X = np.real(cf_val)

    S_T = S0 * np.exp(r * T) * np.exp(X_T) / analytic_mean_X
    return S_T
