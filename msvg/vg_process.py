"""Variance Gamma process implementation."""

import numba as nb
import numpy as np


class VGParams:
    def __init__(self, sigma, nu, theta):
        self.sigma = float(sigma)
        self.nu = float(nu)
        self.theta = float(theta)

    def char_exponent(self, u):
        """Lévy exponent ψ(u) such that E[e^{i u X_t}] = exp(t * ψ(u))."""
        u = np.asarray(u, dtype=complex)
        term = 1.0 - 1j * u * self.theta * self.nu + 0.5 * (self.sigma**2) * self.nu * (u**2)
        return -(1.0 / self.nu) * np.log(term)


def vg_cf(u, T, vg):
    """Characteristic function of X_T for a single VG process."""
    psi = vg.char_exponent(u)
    return np.exp(T * psi)


@nb.jit(nopython=True)
def _vg_increment(dt, sigma, nu, theta, size=1):
    """Generate VG log-return increment(s) over time dt."""
    G = np.random.standard_gamma(dt / nu, size=size) * nu
    Z = np.random.standard_normal(size=size)
    dX = theta * G + sigma * np.sqrt(G) * Z
    return dX
