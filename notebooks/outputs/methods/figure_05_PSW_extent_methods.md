# Figure 5 Methods
Script: figure_05_PSW_extent.ipynb

## PSW Definition
  Salinity < 34.5 psu AND sigma0+1000 < 1027.7 kg m-3
  (sigma0 computed via TEOS-10 gsw library)

## PSW Thickness
  Vertical integration using numpy.gradient(depth_vals) layer widths.

## Piecewise Trend Analysis
  Breakpoint year: 2015
  Period 1: 1993–2014 (year < 2015)
  Period 2: 2015–2025 (year >= 2015)
  Mann-Kendall: Yue & Wang (2004) autocorrelation-corrected variant
  Bootstrap CI: 95%, n=1000 resamples, seed=42
  Rolling mean: 12-month centred; first/last 6 months set to NaN

## Scatter Validation
  IGP 2018 CTD/XCTD and KH2025 CTD profiles collocated to daily GLORYS12.
  Minimum observed PSW thickness threshold: 10.0 m

## Data Sources
  Ocean reanalysis: GLORYS12 (1/12 degree, monthly)
  Bathymetry: ETOPO1 (via rockhound)
  In-situ: IGP 2018 CTD/XCTD, KH2025 CTD
