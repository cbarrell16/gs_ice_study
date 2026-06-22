# Figure 6: Methodology

## Surface Energy Budget and Cold Air Outbreak Index

### Data Sources

**ERA5 Reanalysis** (Hersbach et al., 2020)
- **Temporal Coverage**: 1979-2025
- **Spatial Resolution**: 0.25° × 0.25°
- **Temporal Resolution**: Monthly means
- **Region**: Greenland Sea

### Panel A: Surface Energy Budget

#### Budget Equation

The total surface energy flux is calculated as:

F₀ = F_SW,net + F_LW,net + F_SH + F_LH

**Sign convention**: Positive = downward flux (energy into ocean surface)

#### Unit Conversion

ERA5 provides daily accumulated fluxes (J m⁻²) averaged to monthly means.
Conversion to W m⁻²: F = [F_accumulated × days_per_month] / seconds_per_month

#### Spatial Masking

Three masks applied: Greenland Sea polygon, ocean only (lsm = 0),
sea ice concentration < 15%.

### Panel B: Cold Air Outbreak (CAO) Index

CAO Index = θ_skin − θ_atmosphere(p)

Default pressure level: 850 hPa. Positive values indicate cold air
over warm ocean, driving enhanced turbulent heat fluxes.

### Seasonal Definitions

- **Early Winter (ONDJ)**: October–January (labelled by year of January)
- **Late Winter (FMA)**: February–April

### Statistical Analysis

Split-trend periods: 1979–2015 and 2015–2025.
Breakpoint pre-specified at 2015 on physical grounds.
Trend rates reported per decade. Significance: ** (p<0.01), * (p<0.05).
Bootstrap CI: n=1000 resamples, 95% prediction bands.

## References

Hersbach, H., et al. (2020). The ERA5 global reanalysis. *QJRMS*, 146(730), 1999-2049.
