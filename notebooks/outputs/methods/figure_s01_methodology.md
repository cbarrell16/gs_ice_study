# Figure S1 — Methodology

## Overview
GLORYS12 sea ice is evaluated against three independent observational datasets using monthly scatter comparisons.

## Panel (a): Fram Strait sea ice export
- **Observations**: De Steur et al. mooring-based monthly sea ice volume flux estimates at Fram Strait (79°N, 20°W–12°E).
- **GLORYS12**: Sea ice volume transport computed as the integral of `siconc × sithick × vsi` across the Fram Strait transect at 79°N. Grid cell widths computed using the Haversine formula. Transport converted from m³ s⁻¹ to km³ month⁻¹ using actual days per month. Sign convention: positive = southward (export).
- **Comparison**: Overlapping period only; GLORYS12 interpolated to observation time steps using nearest-neighbour matching.

## Panel (b): Greenland Sea sea ice drift speed
- **Observations**: OSISAF sea ice drift products OSI-455 (primary) and OSI-405 (gap-fill where OSI-455 is unavailable), pre-processed to Greenland Sea monthly mean speed (km day⁻¹).
- **GLORYS12**: Collocated monthly mean speed from the same domain.
- **Merging**: OSI-455 is used preferentially; OSI-405 fills months with no OSI-455 data to avoid double-counting the overlapping period.
- **Sign corrections**: u-component sign correction applied throughout for OSI-405; v-component sign correction applied for 2009-12 to 2015-05.

## Panel (c): Sea ice thickness
- **Observations**: ESA CCI / AWI CryoSat-2 L3 sea ice thickness, filtered to status_flag == 0 (nominal retrieval) and quality_flag == 0 (nominal quality). Negative values excluded.
- **GLORYS12**: `sithick` extracted at the nearest grid cell to each valid CCI observation point for the same month.
- **Domain**: Greenland Sea polygon. Winter months only (October–April).
- **Scatter**: Each point represents one valid CCI grid cell collocated with the nearest GLORYS12 grid cell.

## Statistics
Pearson correlation (r), bias (GLORYS12 − observations), RMSE, and linear regression slope computed over all valid pairs. Significance threshold: p < 0.001.

## Panel (a) statistics
- n = 289
- r = 0.869 (p < 0.001)
- Bias = 10.34 km³ month⁻¹
- RMSE = 62.10 km³ month⁻¹
- Slope = 0.793

## Panel (b) statistics (OSI-455 priority merge)
- n = 391
- r = 0.897 (p < 0.001)
- Bias = 0.39 km day⁻¹
- RMSE = 2.15 km day⁻¹
- Slope = 0.822

## Panel (c) statistics
- n = 1643
- r = 0.292 (p < 0.001)
- Bias = -0.162 m
- RMSE = 1.177 m
- Slope = 0.104
