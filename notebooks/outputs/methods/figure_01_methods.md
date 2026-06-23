# Figure 1: Methodology

## Overview

Panels (a) and (b) show the **annual maximum sea ice extent** extracted from
daily OSISAF Sea Ice Index data. For each calendar year, the maximum SIE
value and its date are identified across all daily observations. Trend fitting,
bootstrap confidence intervals (95%, n=1000), and Mann-Kendall significance
testing are applied to the resulting annual-maximum series.

Split linear trend breakpoints (Pan-Arctic: 2017; Greenland Sea: 2015) are
physically motivated by piecewise linear regression logged
during script execution.

Spatial panels (c) and (d) use March ERA5 SIC for the ice-edge contour and
trend field masking (15% threshold). The representative month can be
overridden via FORCE_P1_MONTH / FORCE_P2_MONTH if needed.

An additional output (`annual_max_sie_dates.csv`) records the date of the
annual maximum for both regions.

## Spatial Sea Ice Concentration Trends

### Data Sources
- **ERA5 Reanalysis**: Monthly sea ice concentration from ECMWF ERA5
  (Hersbach et al., 2020)
- **Temporal Coverage**: 1979-2025
- **Spatial Resolution**: 0.25° × 0.25°

### Processing Methods
SIC data were extracted for March and subset to the Arctic domain. Linear
trends were calculated at each grid cell using ordinary least squares
regression. Trends are reported in % decade⁻¹ (slope × 10 yr × 100).
Only grid cells with ≥5 valid observations were included. Spatial trends
were masked where March SIC < 15%.

**Two temporal periods were analyzed:**
- Period 1: 1979-2015 (37 years)
- Period 2: 2015-2025 (10 years)

## Annual Maximum Sea Ice Extent Timeseries

### Data Sources
- **OSI SAF Sea Ice Index** (daily): Pan-Arctic and Greenland Sea regions
  (OSI SAF, 2017)
- **Temporal Coverage**: 1979-2026

### Annual Maximum Extraction
For each calendar year, the daily SIE value and its date were identified
as the annual maximum across all daily observations within that year.
No seasonal restriction was applied — the true calendar-year maximum
is used, which typically occurs in late February or March for both regions
but may differ by year.

### Statistical Methods
- Split linear trends at predetermined breakpoints
  (Pan-Arctic: 2017; Greenland Sea: 2015)
- Bootstrap confidence intervals (95%, n=1000)
- Mann-Kendall trend test
- Chow test for trend comparison (Greenland Sea only)

## References

Hersbach, H., et al. (2020). The ERA5 global reanalysis.
  *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.

OSI SAF (2017). Global Sea Ice Concentration Climate Data Record v2.0.
  EUMETSAT SAF on Ocean and Sea Ice. https://osi-saf.eumetsat.int/
