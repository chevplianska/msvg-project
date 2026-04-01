"""Markov-switching Variance Gamma process implementation."""

import numba as nb
import numpy as np


@nb.jit(nopython=True)
def _vg_increment_markov(dt, sigma, nu, theta, size=1):
    """VG increment helper for Markov chain."""
    G = np.random.standard_gamma(dt / nu, size=size) * nu
    Z = np.random.standard_normal(size=size)
    dX = theta * G + sigma * np.sqrt(G) * Z
    return dX


@nb.jit(nopython=True, parallel=True)
def _markov_mc_kernel(n_sims, n_steps, dt, lam01, lam10, s0, n0, t0, s1, n1, t1, p0, seed=42):
    """Monte Carlo engine for Markov-switching VG (parallel)."""
    X_T = np.empty(n_sims)

    for i in nb.prange(n_sims):
        np.random.seed(seed + i)
        state = 0 if np.random.random() < p0 else 1
        x = 0.0

        for _ in range(n_steps):
            if state == 0:
                nu = n0
                theta = t0
                sigma = s0
                lam = lam01
            else:
                nu = n1
                theta = t1
                sigma = s1
                lam = lam10

            dX = _vg_increment_markov(dt, sigma, nu, theta, size=1)[0]
            x += dX

            if np.random.random() < lam * dt:
                state = 1 - state

        X_T[i] = x

    return X_T


def markov_vg_cf(u, T, vg0, vg1, lam01, lam10, p0):
    """
    CF for X_T in the 2-state VG Markov model (Prop. 2 in Konikov-Madan).
    """
    u = np.atleast_1d(u).astype(complex)

    phi0_1 = np.exp(vg0.char_exponent(u))
    phi1_1 = np.exp(vg1.char_exponent(u))

    with np.errstate(divide='ignore', invalid='ignore'):
        lam = np.log(phi0_1) - np.log(phi1_1)

    temp = 0.5 * (lam + lam10 - lam01)
    disc_sq = temp * temp + lam10 * lam01
    disc = np.sqrt(disc_sq)

    eta1 = temp - disc
    eta2 = temp + disc

    denom = eta2 - eta1
    denom = np.where(np.abs(denom) < 1e-16, 1e-16 + 0j, denom)

    exp_front = np.exp(-(eta1 + lam01) * T)
    exp_eta = np.exp(-(eta2 - eta1) * T)

    with np.errstate(divide='ignore', invalid='ignore'):
        g0 = exp_front * (eta2 + lam01 - (eta1 + lam01) * exp_eta) / denom
        g1 = (
            (1.0 / lam01)
            * exp_front
            * (eta2 * (eta1 + lam01) * exp_eta - eta1 * (eta2 + lam01))
            / denom
        )

    g = p0 * g0 + (1.0 - p0) * g1

    with np.errstate(divide='ignore', invalid='ignore'):
        phi0_T = np.exp(T * np.log(phi0_1))
    cf_vals = phi0_T * g

    return cf_vals
