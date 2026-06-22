# Figure 3: Methodology

## Temperature and Salinity Multi-Panel Analysis

### Data Sources

**GLORYS12V1 Ocean Reanalysis** (Lellouche et al., 2021)
- **Variables**: Potential temperature (thetao), Practical salinity (so)
- **Temporal Coverage**: 1993-2025
- **Spatial Resolution**: 1/12° (~8 km)
- **Vertical Resolution**: 50 depth levels (0-5500m)
- **Region**: Greenland Sea (bounded by custom polygon)

### Depth Ranges

Three depth layers analyzed:
- **Surface**: 0-50 m
- **Intermediate**: 50-250 m
- **Deep**: 250-1000 m

Depth averaging performed by selecting depth range and computing mean over depth dimension, then spatial averaging over latitude/longitude.

### Figure 3 Panels A & B: Multi-Depth Timeseries with Split Trends

#### Data Processing
1. **Depth averaging**: Mean over specified depth range
2. **Spatial averaging**: Mean over Greenland Sea region
3. **Temporal smoothing**: 12-month centered rolling mean to reduce high-frequency variability

#### Split-Trend Analysis

**Breakpoint**: 2015 (pre-specified on physical grounds)

**Periods**:
- Period 1: 1993-2015 (display label; data mask is year < 2015, i.e. up to Dec 2014)
- Period 2: 2015-2025

For each depth layer and period:

**Linear regression**:
```
y = β₀ + β₁x
```
where y is the variable value, x is decimal year (year + month/12)

**Trend expressed as**: Change per decade = 10 × β₁

#### Statistical Testing

**Modified Mann-Kendall Test** (Yue & Wang, 2004)
- Non-parametric test for monotonic trend with autocorrelation correction
- Variance of the MK statistic corrected using serial correlation coefficients at all lags
- Accounts for positive autocorrelation in monthly timeseries, which would otherwise
  inflate the probability of detecting spurious trends
- Kendall's tau (τ) measures strength and direction of trend
- Significance levels: *** (p < 0.001), ** (p < 0.01), * (p < 0.05)

**Bootstrap Confidence Intervals** (Efron & Tibshirani, 1993)
- 1000 bootstrap resamples with replacement
- 95% confidence intervals from 2.5th and 97.5th percentiles
- Displayed as shaded regions around trend lines

### Figure 3 Climatology Panels C & D: Surface Layer Seasonal Climatology

#### Depth Layer
Analysis restricted to surface layer (0-50 m) to capture seasonal cycle in upper ocean.

#### Decadal Climatologies

Mean seasonal cycles calculated for four periods:
- **1990s**: 1993-1999 (partial decade, GLORYS12 starts 1993)
- **2000s**: 2000-2009
- **2010s**: 2010-2019
- **2020s**: 2020-2024

**2025**: Shown separately (incomplete year)

**Climatological Mean**: Full 1993-2025 average

#### Calculation Method

For each decade:
1. Extract all data within decade
2. Group by month (1-12)
3. Calculate mean across all years in decade
4. Result: 12 monthly mean values

This preserves seasonal structure while showing decadal evolution.

### Physical Interpretation

#### Temperature Trends
- **Surface warming** (0-50m): Indicates atmospheric warming, reduced sea ice cover
- **Intermediate warming** (50-250m): Atlantic Water influence (Atlantification)
- **Deep layer**: Relatively stable, insulated from surface forcing

#### Salinity Trends
- **Surface freshening**: Increased ice melt, reduced brine rejection, precipitation changes
- **Intermediate layer**: Balance between Atlantic inflow and local modification
- **Deep layer**: Long-term water mass changes

#### Seasonal Climatology
- **Winter maximum T/S**: Convective mixing, Atlantic Water inflow
- **Summer minimum T/S**: Ice melt, solar heating, freshwater stratification
- **Decadal shifts**: Changing balance of ice formation, melt, and ocean heat transport

## References

Efron, B., & Tibshirani, R. J. (1993). *An Introduction to the Bootstrap*. Chapman & Hall/CRC.

Kendall, M. G. (1975). *Rank Correlation Methods* (4th ed.). Charles Griffin.

Lellouche, J.-M., et al. (2021). The Copernicus Global 1/12° Oceanic and Sea Ice GLORYS12 Reanalysis. *Frontiers in Earth Science*, 9, 698876. https://doi.org/10.3389/feart.2021.698876

Mann, H. B. (1945). Nonparametric tests against trend. *Econometrica*, 13(3), 245-259.

Yue, S., & Wang, C. (2004). The Mann-Kendall test modified by effective sample size to detect trend in serially correlated hydrological series. *Water Resources Management*, 18(3), 201-218. https://doi.org/10.1023/B:WARM.0000043140.61082.60

## Software

Analysis performed using:
- Python 3.10.12
- xarray for NetCDF data handling
- pymannkendall for modified Mann-Kendall test (Yue & Wang, 2004)
- SciPy for statistical tests (linear regression)
- NumPy for bootstrap resampling
- Matplotlib for visualization
