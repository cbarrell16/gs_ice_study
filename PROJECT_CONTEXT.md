# Greenland Sea Ice Study - Project Context for Claude

## Critical Rules (ALWAYS FOLLOW)

### 1. Scientific Rigor - NEVER Modify Without Permission
- **DO NOT** change data sources (ERA5, OSISAF, GLORYS12, mooring data, Argo, IGP)
- **DO NOT** change data processing methods or calculations
- **DO NOT** change statistical methods
- **ONLY** change presentation/plotting when explicitly requested
- If unsure whether something counts as "processing" vs "presentation", ASK FIRST

### 2. Every Script Must Include
- **Logging**: Use `utils/logger.py` with setup_logger, log_data_loading, log_processing_step, log_output_file, log_completion
- **Methods documentation**: Auto-generate detailed `outputs/methods/figure_XX_methods.md` with:
  - Data sources with citations
  - Mathematical formulations
  - Statistical methods
  - References to scientific literature
- **Processed data output**: Save intermediate data as .nc or .csv files to `outputs/processed_data/figure_XX/`
- **Version info**: Include version number and last modified date in docstring

### 3. Code Organization Principles
- Keep notebooks for now (will convert to .py scripts later)
- Extract common functions to utils files as we go
- Use config.yaml for all parameters (don't hardcode)
- Output structure: `outputs/{figures,processed_data,logs,methods}/`

---

## Project Structure

```
gs_ice_study/
├── config.yaml              # Central configuration
├── utils/
│   ├── __init__.py
│   ├── logger.py           # Logging utilities
│   ├── data_utils.py       # (to be created)
│   ├── stats_utils.py      # (to be created)
│   └── plot_utils.py       # (to be created)
├── notebooks/
│   ├── figure_01_spatial_and_timeseries.ipynb
│   ├── figure_s1_piecewise_and_ssa.ipynb
│   └── ...
├── outputs/
│   ├── figures/
│   ├── processed_data/
│   ├── logs/
│   └── methods/
└── data/                    # Reference only (actual data in ../)
```

---

## Data Sources (DO NOT CHANGE)

### Primary Data Locations
- **ERA5**: `../era5/era5_*_Arctic.nc`
- **OSISAF**: `../osi-sea_ice_index/`
- **GLORYS12**: `../glorys/GLORYS12*.nc`
- **Fram Strait Moorings**: `../fram_strait_moorings/`
- **Argo**: Accessed via `argopy` with erddap source
- **IGP (2018 field campaign)**: `../igp/` (FTP download required)

### Data Source Rules
- **ETOPO1**: ALWAYS use `rh.fetch_etopo1(version="ice")` - NOT fetch_earth_relief
- **OSISAF**: Load from files, use region='nh' for pan-Arctic, region='fram' for Greenland Sea
- **GLORYS**: Monthly output, avoid parallel=True (memory issues)
- **Mooring data**: Already corrected for velocity sign errors in processed files

### Known Data Issues (Already Handled)
- OSISAF historical velocity sign error (corrected in processing)
- Mooring temporal gaps (coverage thresholds applied)
- ERA5 time coordinate inconsistencies (handled during loading)

---

## Key Analysis Parameters

### Regions
**Greenland Sea Polygon:**
```python
GREENLAND_SEA_COORDS = [(-22, 71), (-8.5, 71), (12, 79), (-21, 79), (-28, 73), (-22, 71)]
```

**Fram Strait Moorings:**
```python
MOORINGS = {'F17': -8.0, 'F14': -6.5, 'F13b': -5.5, 'F13': -5.0,
            'F12': -4.0, 'F11': -3.0, 'F10': -2.0}
MOORING_LAT = 79.0
```

### Time Periods
- **Period 1**: 1979-2014
- **Period 2**: 2015-2025
- **Breakpoint year**: 2015 (Greenland Sea), 2017 (pan-Arctic)
- **Max extent years**: 1986 (P1), 2023 (P2)

### Statistical Parameters
- **Confidence level**: 0.95
- **Bootstrap iterations**: 1000-10000
- **SIC threshold**: 0.15 (15%)
- **SSA window fraction**: 0.15

---

## Standard Colors & Styling

### Colors (from config.yaml)
```python
COLOR_PERIOD1 = '#2E86AB'      # GLORYS blue
COLOR_PERIOD2 = '#A23B72'      # Purple-red
COLOR_DATA = '#808080'         # Gray
COLOR_BOUNDARY = '#000000'     # Black
COLOR_MOORING = '#800080'      # Purple
COLOR_ICE_EDGE = '#00008B'     # Dark blue
COLOR_BREAKPOINT = '#808080'   # Gray
```

### Plotting Standards
- **DPI**: 600
- **Figure sizes**: Defined in config.yaml
- **Font**: DejaVu Sans (default), monospace for stats boxes
- **Alpha values**: relief=0.5, trend=0.7, ci_band=0.15

### Diverging Colormap for Trends
```python
colors_trend = ['#2166ac', '#4393c3', '#92c5de', '#d1e5f0', 'white',
                '#fddbc7', '#f4a582', '#d6604d', '#b2182b']
```

---

## Units (MUST BE CONSISTENT)

```python
UNITS = {
    'sie': '×10⁶ km²',
    'sie_rate': '×10⁶ km² yr⁻¹',
    'sie_decade': '×10⁶ km² decade⁻¹',
    'sic': '%',
    'sic_rate': '% yr⁻¹',
    'sic_decade': '% decade⁻¹',
    'temperature': '°C',
    'salinity': 'psu',
    'depth': 'm',
    'velocity': 'm s⁻¹'
}
```

### Important Unit Conversions
- **SIC spatial trends**: slope (yr⁻¹) × 1000 = % decade⁻¹
  - Factor breakdown: 10 years × 100 (for %)
  - Therefore: vmax_trend = 25 when data multiplied by 1000

---

## Common Functions (Extract to Utils)

### Already Defined (Don't Recreate)
- `calculate_spatial_trends_vectorized()` - Linear trends for grid cells
- `bootstrap_trend_ci()` - Bootstrap confidence intervals
- `mann_kendall_test()` - Non-parametric trend test
- `analytical_trend_ci()` - Parametric confidence intervals
- `compare_trends()` - Chow test for trend differences
- `perform_ssa_analysis()` - SSA decomposition
- `add_months()` - Add month coordinate to xarray
- `fetch_sie()` - Get region from OSISAF list

---

## Matplotlib LaTeX Tips

### CRITICAL: Use Single Backslash in Raw Strings
```python
# CORRECT:
ax.set_ylabel(r'Sea ice extent ($\times10^{6}$ km$^{2}$)', fontsize=10)

# WRONG:
ax.set_ylabel(r'Sea ice extent ($\\times10^{6}$ km$^{2}$)', fontsize=10)
```

### Common LaTeX Commands
- Multiplication: `$\times$`
- Superscript: `$x^{2}$`
- Subscript: `$x_{i}$`
- Degree: `$°$` or `$^{\circ}$`

---

## Research Context (From User Memory)

### Project Overview
Analysis of Greenland Sea ice dynamics, ocean-atmosphere interactions, and water mass transformations. Focus on:
- Counterintuitive regional ice increases vs Arctic decline
- Atlantification processes
- Water mass transformation reorganization

### Key Collaborators & Data
- **Laura de Steur**: Fram Strait mooring data
- **IGP 2018**: Field campaign data (user participated during PhD)
- **Argo floats**: Use erddap source (more stable than other sources)

### Current Status
- Building clean set of notebooks for paper submission
- Near completion of draft figures
- Will receive feedback from collaborators soon
- Planning GitHub repo (private initially, public upon publication)

### Workflow Preferences
- Iterative approach to problem-solving
- Systematic validation before implementation
- Step-by-step verification of issues
- Comprehensive documentation

---

## GitHub Setup

**Repository**: Private (will be made public with DOI via Zenodo upon publication)

**Not in Git**:
- Logs (too verbose)
- Original data (too large, document sources instead)
- Possibly large processed files (evaluate case-by-case)

**In Git**:
- All notebooks
- Utility modules
- Config files
- Processed data for figures (enables replotting)
- Methods documentation
- README

---

## Common Pitfalls to Avoid

1. **Memory Issues**
   - NEVER use `parallel=True` with xarray for ERA5/GLORYS
   - Process year-by-year for large datasets
   - Check for existing output to avoid reprocessing

2. **Data Quality**
   - Always validate sign of velocity components
   - Check for temporal gaps in mooring data
   - Filter incomplete seasons (count months per season)

3. **Statistical Rigor**
   - Use monthly data for trends (not yearly aggregation)
   - Match variable types (in situ vs potential temperature)
   - Apply TEOS-10 conversions when needed (use gsw package)

4. **Attribution**
   - Proper citation of data sources
   - Campaign participation affects attribution requirements

---

## Next Steps (When Relevant)

1. **Utility Modules**: Extract common functions to:
   - `data_utils.py` - Data loading, region subsetting
   - `stats_utils.py` - Statistical methods
   - `plot_utils.py` - Plotting helpers

2. **Wrapper Script**: Easy execution of all figures with single command

3. **Publication Prep**:
   - Finalize all figures
   - Complete methods documentation
   - Add README with reproducibility instructions
   - Create Zenodo deposit for DOI

---

## When Starting New Chat

**Paste this document** along with:
1. Specific question/task
2. Any relevant error messages
3. Which figure/analysis you're working on

This ensures I have all context needed to help effectively!

---

## Version History

- **v1.0** (2026-02-27): Initial context document created
- Project initiated with Figure 1 and S1 refactoring
- Logger utility and config.yaml structure established
