# Figure S1: Methodology

## Piecewise Linear Regression

### Method
Piecewise linear regression (PWLR) identifies structural breaks in timeseries data by fitting multiple linear segments with automated breakpoint detection (Muggeo, 2003; Toms & Lesperance, 2003).

The method minimizes the sum of squared residuals while determining optimal breakpoint locations:

minimize: Σᵢ (yᵢ - ŷᵢ)²

where ŷᵢ is the predicted value from the appropriate linear segment.

### Implementation
- **Software**: `pwlf` Python package (Jekel et al., 2019)
- **Number of segments**: 2 (one breakpoint)
- **Optimization**: Davies' algorithm for breakpoint estimation

For each segment, standard linear regression statistics were calculated:
- Coefficient of determination (R²)
- Slope significance (p-value from t-test)

### Interpretation
The identified breakpoints represent statistically significant changes in trend direction or magnitude. For March sea ice extent:
- **Pan-Arctic**: Breakpoint ≈ 2017
- **Greenland Sea**: Breakpoint ≈ 2015

These breakpoints justify the use of split linear trends in Figure 1.

## Singular Spectrum Analysis (SSA)

### Method
SSA is a non-parametric time series decomposition technique that separates trends, oscillations, and noise without assuming functional forms (Golyandina et al., 2001; Hassani, 2007).

The method embeds the time series in a trajectory matrix using lagged vectors:

X = [x₁, x₂, ..., xₙ]  
Window size L determines the dimension of embedding

Singular Value Decomposition (SVD) decomposes the trajectory matrix:
X = Σᵢ λᵢ Uᵢ Vᵢᵀ

where λᵢ are singular values, and Uᵢ, Vᵢ are left and right singular vectors.

### Implementation
- **Software**: `pyts` Python package (Faouzi & Janati, 2020)
- **Window size**: 15% of time series length (≈ 7 years for March data)
- **Trend extraction**: Sum of first two principal components (capturing low-frequency variability)
- **Extrema detection**: Local maxima/minima identified using `scipy.signal.find_peaks`

### Parameters
- **Minimum peak distance**: 5% of time series length (prevents detection of spurious extrema)
- **Prominence threshold**: Not applied (all local extrema included)

### Interpretation
SSA-derived trends reveal:
- **Pan-Arctic**: Multi-decadal decline with superimposed variability
- **Greenland Sea**: Higher-frequency variability with recent reversal

Extrema (peaks/troughs) identify periods of maximum/minimum extent within the SSA-smoothed trend, highlighting characteristic timescales of variability.

## Statistical Validation

### Mann-Kendall Test
Both PWLR segments and SSA trends were tested for monotonic trends using the Mann-Kendall test:
- H₀: No monotonic trend
- H₁: Monotonic increasing or decreasing trend
- Significance: α = 0.05

### Advantages of Multi-Method Approach
1. **PWLR**: Identifies discrete regime shifts
2. **SSA**: Reveals continuous low-frequency variability
3. **Complementary**: PWLR for breakpoints, SSA for smooth trends

Together, these methods provide robust characterization of non-stationary sea ice extent dynamics.

## References

Faouzi, J., & Janati, H. (2020). pyts: A Python package for time series classification. *Journal of Machine Learning Research*, 21(46), 1-6.

Golyandina, N., Nekrutkin, V., & Zhigljavsky, A. (2001). *Analysis of Time Series Structure: SSA and Related Techniques*. Chapman & Hall/CRC.

Hassani, H. (2007). Singular Spectrum Analysis: Methodology and Comparison. *Journal of Data Science*, 5(2), 239-257.

Jekel, C. F., Venter, G., Venter, M. P., Stander, N., & Haftka, R. T. (2019). Similarity measures for identifying material parameters from hysteresis loops using inverse analysis. *International Journal of Material Forming*, 12(3), 355-378.

Muggeo, V. M. R. (2003). Estimating regression models with unknown break-points. *Statistics in Medicine*, 22(19), 3055-3071.

Toms, J. D., & Lesperance, M. L. (2003). Piecewise regression: A tool for identifying ecological thresholds. *Ecology*, 84(8), 2034-2041.

## Software

Analysis performed using:
- Python 3.10.12
- `pwlf` for piecewise linear regression
- `pyts` for Singular Spectrum Analysis
- `scipy` for peak detection and statistical tests
- `xarray` for data handling
- `matplotlib` for visualization
