================================================================================
POLAR SURFACE WATER AND ATLANTIC WATER COMPARISON FIGURE
METHODOLOGY DOCUMENTATION
================================================================================

Generated: 2026-06-22 14:42:20
Script: figure_04_PSW_and_AW.ipynb

================================================================================
1. DATA SOURCES
================================================================================

GLORYS12 Ocean Reanalysis (monthly, 1993-2025)
  Variables used:
    - thetao: Potential temperature (°C)
    - so: Salinity (psu)
    - absolute_density: In-situ density (kg/m³)
    - vo: Meridional velocity (m/s)
    - uo: Zonal velocity (m/s)
    - delta_z: Layer thickness (m)
  Horizontal resolution: ~1/12° (~9 km)
  Vertical levels: 50 depth levels

================================================================================
2. WATER MASS DEFINITIONS
================================================================================

2.1 Polar Surface Water (PSW)
  Definition: S < 34.5 psu AND ρ < 1027.7 kg/m³
  Location: Fram Strait (79°N, -20°W to 12°E)
  Depth range: All depths
  Rationale: Captures fresh, low-density Arctic outflow
  Note: absolute_density is in-situ density (kg/m³) computed via
        TEOS-10 from GLORYS12 temperature, salinity, and pressure;
        it is a derived variable in the pre-processed GLORYS12
        collocated files, not a native Copernicus download variable.

2.2 Atlantic Water (AW)
  Definition: GEOGRAPHIC (lon > 5°E AND depth < 550 m)
  Location: Eastern Greenland Sea boundary
              Diagonal from (-8.5°, 71°N) to (12°E, 79°N)
  Rationale: Captures main AW inflow corridor without
             temperature/salinity thresholds that may
             vary with climate change

================================================================================
3. NET TRANSPORT CALCULATIONS
================================================================================

3.1 PSW Net Transport at Fram Strait
  Formula: Transport = -vo × PSW_mask × dz × dx
           where PSW_mask = 1 where PSW criteria met, 0 elsewhere
  dx calculation: Haversine distance between longitude points
  Sign convention: Positive = southward (into Greenland Sea)
  Units: Sv (Sverdrups = 10^6 m³/s)
  Integration: Sum over depth and longitude dimensions

3.2 AW Net Transport at Eastern Boundary
  Method: Normal velocity component through diagonal boundary
  Steps:
    1. Define 100 interpolation points along diagonal boundary
    2. Filter to points where lon > 5°E
    3. Select depths < 550 m
    4. Calculate normal vector (perpendicular to boundary)
       Normal = (dy_line, dx_line) / ||(dy_line, dx_line)||
    5. Calculate normal velocity: v_normal = nx × u + ny × v
    6. Calculate transport through each segment:
       Transport_segment = v_normal × dz × ds
       where ds = haversine distance between points
    7. Sum all segments
  Sign convention: Positive = into Greenland Sea (westward)
  Units: Sv (Sverdrups = 10^6 m³/s)

================================================================================
4. PROPERTY CALCULATIONS
================================================================================

4.1 PSW Properties
  Method: Weighted mean where PSW exists
  Formula: Mean_T = sum(T × PSW_mask) / sum(PSW_mask)
           Mean_S = sum(S × PSW_mask) / sum(PSW_mask)
  Integration: Over depth and longitude at Fram Strait

4.2 AW Properties
  Method: Simple mean in geographic region
  Formula: Mean_T = mean(T) over filtered points and depths
           Mean_S = mean(S) over filtered points and depths
  Integration: Over interpolation points (lon > 5°E) and depths < 550 m

================================================================================
5. STATISTICAL ANALYSIS
================================================================================

5.1 Linear Trend Analysis
  Method: Piecewise linear regression with fixed breakpoint
  Breakpoint year: 2015 (pre-specified on physical grounds)
  Period 1: 1993-2015
  Period 2: 2015-2025
  Fitting: Ordinary least squares (scipy.stats.linregress)
  Units: Original units per decade (slope × 3652.5)

5.2 Significance Testing
  Test: Modified Mann-Kendall trend test (Yue & Wang, 2004)
  Correction: Variance corrected using serial correlation coefficients
              at all lags to account for autocorrelation in monthly
              timeseries
  Null hypothesis: No monotonic trend
  Significance levels:
    * p < 0.05
    ** p < 0.01
    *** p < 0.001
  References:
    Yue, S., & Wang, C. (2004). Water Resources Management, 18(3), 201-218.
    https://doi.org/10.1023/B:WARM.0000043140.61082.60

5.3 Uncertainty Quantification
  Method: Bootstrap resampling
  Iterations: 1000
  Confidence level: 95%
  Procedure:
    1. Randomly resample data with replacement
    2. Calculate trend for bootstrap sample
    3. Repeat 1000 times
    4. Extract 2.5th and 97.5th percentiles
  Reference:
    Efron & Tibshirani (1994). An Introduction to the Bootstrap.

5.4 Rolling Mean Smoothing
  Window: 12 months, centred
  Minimum periods: 6
  Boundary masking: First and last 6 months set to NaN
  Rationale: Centred windows are underpopulated near record ends,
             causing spurious edge curvature; masking prevents this.
             Monthly data continues to record endpoints.

================================================================================
6. VISUALIZATION
================================================================================

Figure Layout: 6 panels (3 rows × 2 columns)
  Column 1: Polar Surface Water (PSW)
  Column 2: Atlantic Water (AW)
  Row 1: Net transport (Sv)
  Row 2: Temperature (°C)
  Row 3: Salinity (psu)

Panel Elements:
  - Monthly data: solid line, α=0.4
  - 12-month rolling mean: solid line, lw=2.0, α=0.9
  - Trend lines: dashed, linewidth=2.5, α=0.9
  - Bootstrap CI: shaded region, α=0.15
  - Breakpoint: gray dotted vertical line
  - Zero line: gray horizontal (transport panels only)
  - Grid: α=0.3

Colors:
  PSW: #2E86AB (blue)
  AW: #F77F00 (orange)

================================================================================
7. REFERENCES
================================================================================

GLORYS12 Reanalysis:
  Lellouche, J.-M., et al. (2021). The Copernicus Global 1/12°
  Oceanic and Sea Ice GLORYS12 Reanalysis. Frontiers in Earth
  Science, 9, 698876.

Statistical Methods:
  Yue, S., & Wang, C. (2004). The Mann-Kendall test modified by
  effective sample size to detect trend in serially correlated
  hydrological series. Water Resources Management, 18(3), 201-218.
  https://doi.org/10.1023/B:WARM.0000043140.61082.60
  Efron, B., & Tibshirani, R. J. (1994). An Introduction to the
  Bootstrap. CRC Press.

================================================================================
END OF METHODOLOGY DOCUMENTATION
================================================================================
