# FQE Project: Variance Gamma Markov Chain Option Pricing

Replication of "Option Pricing Using Variance Gamma Markov Chains" by Konikov & Madan (2002).

## Structure

```
msvg-project/
├── msvg/                  # Python package with source code for the project
│   ├── vg_process.py      # Single VG process
│   ├── markov_chain.py    # Markov-switching VG
│   ├── option_pricing.py  # FFT pricing (Carr-Madan)
│   ├── utils.py           # Monte Carlo simulation
│   └── calibration.py     # Model calibration
├── notebooks/
│   └── paper_replication.ipynb    # Main notebook: complete replication
└── docs/   # No docs yet, but I put a Markdown version of the Markov VG paper Konikov-Madan (2002) for easy reference.
```

## Installation

```bash
pip install -e .
```

## Notebooks

- **`notebooks/paper_replication.ipynb`**: Complete replication with mathematical explanations and all analysis from Konikov-Madan (2002)

## Source Code in `msvg/`:

### `msvg/vg_process.py`
- `VGParams`: VG parameter class (sigma, nu, theta)
- `vg_cf`: Characteristic function for single VG process

### `msvg/markov_chain.py`
- `markov_vg_cf`: Characteristic function for two-state Markov-switching VG

### `msvg/option_pricing.py`
- `fft_call_price`: FFT-based European call pricing (Carr-Madan)
- `pdf_from_cf`: PDF recovery from characteristic function via numerical integration

### `msvg/utils.py`
- `monte_carlo_single_vg`: Monte Carlo simulation for single VG
- `monte_carlo_markov_vg_numba`: Monte Carlo simulation for Markov VG

### `msvg/calibration.py`
- `calibrate_single_vg`: Calibrate single VG model to market prices
- `calibrate_markov_vg`: Calibrate Markov VG model to market prices

## TODO
- [ ] Add documentation of the source code to the `docs/` folder.
- [ ] Validate against published parameter/price tables from papers to make sure we are implementing the models correctly.
- [ ] Fit to real option prices to evaluate whether the Markov VG model is truly better than the single VG model in capturing the market.
