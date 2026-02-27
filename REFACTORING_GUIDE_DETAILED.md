# Figure 1 and S1 Refactoring Guide

## Overview
Split `Figure_1_SIE_trends_and_S1.ipynb` into two notebooks with specific plotting modifications.

---

## Figure 1: `figure_01_spatial_and_timeseries.ipynb`

### Structure
4 panels (2x2 grid): Spatial maps (a,b) + Split trend timeseries (c,d)

### Components to Include

**From Cell 1 (Spatial Maps):**
- Keep ALL imports, configuration, and functions (lines 28-510)
- Keep data loading: ERA5, ETOPO1, spatial trend calculations
- Keep BOTH Panel A and Panel B plotting code (lines 313-602)

**From Cell 2 (Timeseries):**
- Add imports: `matplotlib.dates`, `pwlf`, `pyts` (if not already present)
- Add ALL statistical functions (lines 747-1015)
- Add OSISAF data loading section (lines 1162-1187)
- Add Panel (a) - Pan-Arctic split trends (lines 1224-1312)
- Add Panel (b) - Greenland Sea split trends (lines 1314-1402)

### Specific Edits Required

#### 1. Spatial Trend Units (Panels a & b)
**Line ~346** and **~528** (both panels):
```python
# BEFORE:
trend_plot = ax.pcolormesh(
    ds_subset.longitude,
    ds_subset.latitude,
    slope_p1_masked.values,  # <-- THIS
    ...
)

# AFTER:
trend_plot = ax.pcolormesh(
    ds_subset.longitude,
    ds_subset.latitude,
    slope_p1_masked.values * 10 * 100,  # Convert to % per decade
    ...
)
```

#### 2. Colorbar Range (Panels a & b)
**Line ~308**:
```python
# BEFORE:
vmax_trend = 0.025  # yr⁻¹

# AFTER:
vmax_trend = 2.5  # % per decade (0.025 * 10 years * 100)
```

#### 3. Colorbar Label
**Line ~582** and **~587**:
```python
# BEFORE:
cbar2.set_label('SIC Trend (yr⁻¹)', fontsize=10)

# AFTER:
cbar2.set_label('SIC Trend (% decade⁻¹)', fontsize=10)
```

#### 4. Gridlines on Top (Panels a & b)
**Line ~474** and **~556**:
```python
# BEFORE:
gl = ax.gridlines(
    draw_labels=True, x_inline=False, y_inline=False,
    linewidth=0.5, color='gray', alpha=0.85, linestyle=':'
)

# AFTER:
gl = ax.gridlines(
    draw_labels=True, x_inline=False, y_inline=False,
    linewidth=0.5, color='gray', alpha=0.85, linestyle=':',
    zorder=20  # <-- ADD THIS to put gridlines on top
)
```

#### 5. Red Squares for Greenland Sea Max Years (Panel d)
Find where maximum extent years are marked in Greenland Sea panel (~line 1380):
```python
# BEFORE:
ax.scatter(year_time, year_data.values[0], s=120, marker='s',
          color=COLOR_MOORING, edgecolors='white', linewidth=1.5,
          zorder=5, alpha=0.8)

# AFTER:
ax.scatter(year_time, year_data.values[0], s=120, marker='s',
          color='red', edgecolors='none',  # Changed from purple to red, no edge
          zorder=5, alpha=0.8)
```

#### 6. Figure Layout
Replace the 6-panel layout with 4-panel:
```python
# BEFORE:
fig = plt.figure(figsize=(12, 10))
gs = fig.add_gridspec(3, 2, hspace=0.2, wspace=0.15, ...)

# AFTER:
fig = plt.figure(figsize=(14, 12))
gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.25,
                      left=0.08, right=0.98, top=0.95, bottom=0.05)
```

#### 7. Panel Labels
- Spatial maps keep (a) and (b)
- Timeseries from "Panel (a)" → "Panel (c)"
- Timeseries from "Panel (b)" → "Panel (d)"

#### 8. Output Path
```python
# BEFORE:
output_file = './Figure1_overview_map.png'
output_path = './sie_trends/Fig2_SIE_trends_winter_6panel_CI.png'

# AFTER:
output_file = './outputs/figures/figure_01.png'
```

#### 9. Add Logging
At start of notebook:
```python
from utils.logger import setup_logger, log_data_loading, log_processing_step, log_output_file, log_completion
from datetime import datetime

logger = setup_logger('figure_01')
start_time = datetime.now()
```

At end:
```python
log_output_file(logger, 'figure', output_file)
log_completion(logger, start_time)
```

---

## Figure S1: `figure_s1_piecewise_and_ssa.ipynb`

### Structure
4 panels (2x2 grid): Piecewise regression (a,b) + SSA decomposition (c,d)

### Components to Include

**From Cell 2 (Timeseries):**
- Imports and configuration (lines 707-741)
- ALL statistical functions (lines 747-1077)
- OSISAF data loading (lines 1162-1187)
- Panel (c) - Pan-Arctic PWLR (lines 1404-1444) → Relabel as Panel (a)
- Panel (d) - Greenland Sea PWLR (lines 1446-1485) → Relabel as Panel (b)
- Panel (e) - Pan-Arctic SSA (lines 1510-1558) → Relabel as Panel (c)
- Panel (f) - Greenland Sea SSA (lines 1560-1608) → Relabel as Panel (d)

### Specific Edits Required

#### 1. Figure Layout
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()
```

#### 2. Panel Labels
- Change "Panel (c)" → "Panel (a)" (PWLR Arctic)
- Change "Panel (d)" → "Panel (b)" (PWLR Greenland)
- Change "Panel (e)" → "Panel (c)" (SSA Arctic)
- Change "Panel (f)" → "Panel (d)" (SSA Greenland)

#### 3. Axis Indexing
```python
# BEFORE:
ax = axes[2]  # Panel (c)
ax = axes[3]  # Panel (d)
ax = axes[4]  # Panel (e)
ax = axes[5]  # Panel (f)

# AFTER:
ax = axes[0]  # Panel (a)
ax = axes[1]  # Panel (b)
ax = axes[2]  # Panel (c)
ax = axes[3]  # Panel (d)
```

#### 4. Output Path
```python
# BEFORE:
output_path = './sie_trends/Fig2_SIE_trends_winter_6panel_CI.png'

# AFTER:
output_path = './outputs/figures/figure_s1.png'
```

#### 5. Configuration
Keep `CONFIG` dict but only relevant settings:
```python
CONFIG = {
    'season': 'winter',
    'n_bootstrap': 1000,
    'confidence_level': 0.95
}
```

---

## Validation Checklist

After creating both notebooks, verify:

- [ ] Figure 1 has 4 panels in 2x2 grid
- [ ] Figure S1 has 4 panels in 2x2 grid
- [ ] Spatial trends show % decade⁻¹ (multiply by 10*100)
- [ ] Colorbar range is ~±2.5 instead of ±0.025
- [ ] Gridlines visible on top of data (zorder=20)
- [ ] Greenland Sea max extent markers are red squares
- [ ] Output paths use new directory structure
- [ ] Panel labels are (a), (b), (c), (d) in both figures
- [ ] All data processing unchanged
- [ ] Logging added to both notebooks

---

## Processing Notes

### Data Not Changed
- ERA5 loading: UNCHANGED
- ETOPO1 loading: UNCHANGED
- OSISAF loading: UNCHANGED
- Spatial trend calculation: UNCHANGED
- Bootstrap CI calculation: UNCHANGED
- PWLR fitting: UNCHANGED
- SSA decomposition: UNCHANGED

### Only Changed
- Panel organization (6 panels → two 4-panel figures)
- Spatial trend display units (yr⁻¹ → % decade⁻¹)
- Gridline zorder (visible on top)
- Marker color for one specific element (purple → red)
- Output file paths
- Added logging

---

## File Locations

Save notebooks to:
- `/local/jbj13rpu/Documents/ROVER/gs_ice_study/notebooks/figure_01_spatial_and_timeseries.ipynb`
- `/local/jbj13rpu/Documents/ROVER/gs_ice_study/notebooks/figure_s1_piecewise_and_ssa.ipynb`
