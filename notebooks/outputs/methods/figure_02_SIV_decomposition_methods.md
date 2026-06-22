# Figure 02 — SIV Decomposition: Methodology Notes

## Data
GLORYS12V1 ocean reanalysis (Lellouche et al., 2021); 1/12° horizontal
grid; variables: `siconc`, `sithick`, `usi`, `vsi`, `cell_area`.
Period: 1993–2025.

## Domain
Greenland Sea polygon: (−22°E, 71°N), (−8.5°E, 71°N), (12°E, 79°N),
(−21°E, 79°N), (−28°E, 73°N). Applied as a 2-D regionmask.

## Budget decomposition
Per-cell SIV (km³) = siconc × sithick × cell_area / 1e9.

Monthly change: dSIV_cell = SIV_cell.diff(time).

Dynamic term (centred-difference flux divergence, negated so
positive = net advective gain):

    dynamic_cell = −∇·(u × h × c) × cell_area × SEC_PER_MONTH / 1e9

where SEC_PER_MONTH = 86400 × 30 s (fixed 30-day approximation).

Thermodynamic residual: thermo_cell = dSIV_cell − dynamic_cell
(positive = local growth, negative = local melt).

## Sign partitioning
Domain-integrated gross terms computed by summing positive and negative
cell contributions separately before seasonal aggregation:
  dynamic import  = Σ max(dynamic_cell, 0)
  dynamic export  = Σ min(dynamic_cell, 0)
  thermo growth   = Σ max(thermo_cell,  0)
  thermo melt     = Σ min(thermo_cell,  0)

## Seasonal aggregation
Early winter: ONDJ (Oct–Jan); seasons labelled by year of January.
Late winter:  FMA  (Feb–Apr); seasons labelled by calendar year.
Incomplete seasons excluded.

## Trend analysis
OLS split at 2015; 95% bootstrap CI (n=1000, seed=42).
Significance: standard Mann-Kendall (scipy.stats.kendalltau);
* p<0.05, ** p<0.01.