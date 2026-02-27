# Figure 1: Methodology

## Spatial Sea Ice Concentration Trends

### Data Sources
- **ERA5 Reanalysis**: Monthly sea ice concentration from ECMWF ERA5 atmospheric reanalysis (Hersbach et al., 2020)
- **Temporal Coverage**: 1979-2025
- **Spatial Resolution**: 0.25° × 0.25°
- **Domain**: Arctic region (60°N-90°N, 90°W-90°E)

### Processing Methods
Sea ice concentration (SIC) data were extracted for March (month of maximum extent) and subset to the Arctic domain. Linear trends were calculated at each grid cell using ordinary least squares regression:

SIC_trend = β₀ + β₁ × year

where β₁ represents the trend in yr⁻¹. Trends were converted to % decade⁻¹ by multiplying by 1000 (10 years × 100 for percentage).

Only grid cells with at least 5 valid observations were included in the trend analysis. Statistical significance was assessed using a two-tailed t-test (α = 0.05).

**Two temporal periods were analyzed:**
- Period 1: 1979-2014 (36 years)
- Period 2: 2015-2025 (11 years)

Spatial trends were masked where March SIC < 15% (ice edge threshold) to focus on ice-covered regions.

### Bathymetry
ETOPO1 ice surface elevation data (Amante & Eakins, 2009) were interpolated to 0.1° resolution for background context.

## Sea Ice Extent Timeseries

### Data Sources
- **OSI SAF Sea Ice Index**: Regional sea ice extent from EUMETSAT Ocean and Sea Ice Satellite Application Facility (OSI SAF, 2017)
- **Regions**: Northern Hemisphere (pan-Arctic) and Fram Strait/Greenland Sea
- **Temporal Coverage**: 1979-2025
- **Temporal Resolution**: Daily, aggregated to monthly means

### Statistical Methods

#### Split Linear Trends
March sea ice extent timeseries were analyzed using split linear trends with predetermined breakpoints:
- **Pan-Arctic**: 2017 (following method of Serreze & Meier, 2019)
- **Greenland Sea**: 2015 (identified from piecewise regression analysis, see Figure S1)

For each period, linear trends were calculated using ordinary least squares regression. Trend significance was assessed using:

1. **Parametric test**: Two-tailed t-test on regression slope (α = 0.05)
2. **Non-parametric test**: Mann-Kendall trend test (Mann, 1945; Kendall, 1975)

The Mann-Kendall test evaluates monotonic trends without assuming linearity or normality. The test statistic S is:

S = Σᵢ₌₁ⁿ⁻¹ Σⱼ₌ᵢ₊₁ⁿ sign(xⱼ - xᵢ)

Kendall's tau (τ) measures correlation:

τ = S / [n(n-1)/2]

#### Uncertainty Quantification
Bootstrap confidence intervals (95%) were calculated for trend estimates using 1000 resamples with replacement (Efron & Tibshirani, 1993). For each bootstrap iteration:
1. Resample time-extent pairs with replacement
2. Fit linear regression
3. Store slope and prediction

Confidence intervals were derived from the 2.5th and 97.5th percentiles of the bootstrap distribution.

#### Trend Comparison
Differences between Period 1 and Period 2 trends were tested using the Chow test (Chow, 1960), which compares:
- H₀: Single pooled trend fits both periods
- H₁: Separate trends are significantly different

The F-statistic tests whether the reduction in residual sum of squares justifies the additional parameters.

## References

Amante, C., & Eakins, B. W. (2009). ETOPO1 1 Arc-Minute Global Relief Model: Procedures, Data Sources and Analysis. NOAA Technical Memorandum NESDIS NGDC-24.

Chow, G. C. (1960). Tests of equality between sets of coefficients in two linear regressions. *Econometrica*, 28(3), 591-605.

Efron, B., & Tibshirani, R. J. (1993). *An Introduction to the Bootstrap*. Chapman & Hall/CRC.

Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049. https://doi.org/10.1002/qj.3803

Kendall, M. G. (1975). *Rank Correlation Methods* (4th ed.). Charles Griffin.

Mann, H. B. (1945). Nonparametric tests against trend. *Econometrica*, 13(3), 245-259.

OSI SAF (2017). Global Sea Ice Concentration Climate Data Record v2.0 - Multimission. EUMETSAT SAF on Ocean and Sea Ice. https://osi-saf.eumetsat.int/

Serreze, M. C., & Meier, W. N. (2019). The Arctic's sea ice cover: trends, variability, predictability, and comparisons to the Antarctic. *Annals of the New York Academy of Sciences*, 1436(1), 36-53.

## Software

Analysis performed using:
- Python 3.10.12
- xarray 2024.x for NetCDF data handling
- SciPy for statistical tests
- Matplotlib and Cartopy for visualization
- Rockhound for bathymetry data access
