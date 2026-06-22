# Figure 02 spatial diagnostics — SIV Spatial Budget: Methodology Notes

## Data
GLORYS12V1 ocean reanalysis (Lellouche et al., 2021); 1/12° horizontal
grid; variables: `siconc`, `sithick`, `usi`, `vsi`, `cell_area`.
Period: 1993–2025.

## Domain
Greenland Sea polygon: (−22°E, 71°N), (−8.5°E, 71°N), (12°E, 79°N),
(−21°E, 79°N), (−28°E, 73°N). Applied as a 2-D regionmask.

## Budget decomposition
Identical to figure_02_SIV_decomposition.py. Per-cell SIV (km³) =
siconc × sithick × cell_area / 1e9. Monthly change dSIV_cell =
SIV_cell.diff(time). Dynamic term from centred-difference flux
divergence, negated (inflow-positive). Thermodynamic residual =
dSIV_cell − dynamic_cell.

Note: SEC_PER_MONTH = 86400 × 30 s (fixed 30-day approximation).

## Seasonal aggregation
Early winter: ONDJ (Oct–Jan); seasons labelled by year of January.
Late winter:  FMA  (Feb–Apr); seasons labelled by calendar year.
Incomplete seasons excluded. 3-D (time, lat, lon) arrays summed
using sel(time=...) on complete-season timesteps.

## Trend maps
OLS slope maps computed per grid cell via apply_ufunc (vectorised).
Years centred before regression for numerical stability.
Slopes converted yr⁻¹ → decade⁻¹ for display.
Per-cell Mann-Kendall available but disabled by default
(COMPUTE_CELL_MK=False) due to computational cost.

## Sign partitioning (growth/melt maps)
Thermodynamic residual clipped to positive (growth) and negative
(melt) before seasonal aggregation, preserving gross spatial terms.