"""Variance Gamma Markov Chain option pricing implementation."""

from .calibration import calibrate_markov_vg, calibrate_single_vg
from .markov_chain import markov_vg_cf
from .option_chain import (
    build_call_surface,
    build_iv_band,
    atm_iv,
    calibrate,
    check_admissible,
    estimate_carry,
    evaluate,
    fit_level,
    implied_rate,
    iv_band_loss,
    load_snapshot,
    market_density_bl,
    pair_call_put,
    prepare_snapshot,
    price_at_level,
    price_msvg,
    price_to_iv,
    price_vg,
    risk_neutral_density,
    scale_to_unit_time,
    score_surface,
    year_fraction,
)
from .option_pricing import fft_call_price, implied_vol, pdf_from_cf
from .utils import monte_carlo_markov_vg_numba, monte_carlo_single_vg
from .vg_process import VGParams, vg_cf

__all__ = [
    "VGParams",
    "vg_cf",
    "markov_vg_cf",
    "fft_call_price",
    "implied_vol",
    "pdf_from_cf",
    "monte_carlo_single_vg",
    "monte_carlo_markov_vg_numba",
    "calibrate_single_vg",
    "calibrate_markov_vg",
    # option-chain pipeline
    "load_snapshot",
    "pair_call_put",
    "estimate_carry",
    "implied_rate",
    "year_fraction",
    "build_call_surface",
    "price_to_iv",
    "build_iv_band",
    "iv_band_loss",
    "score_surface",
    "price_vg",
    "price_msvg",
    "calibrate",
    "check_admissible",
    "evaluate",
    "price_at_level",
    "fit_level",
    "atm_iv",
    "scale_to_unit_time",
    "risk_neutral_density",
    "market_density_bl",
    "prepare_snapshot",
]
