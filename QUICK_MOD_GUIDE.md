# Quick Modification Guide for Notebook Splitting

## Overview
You have the detailed guide. Here are the EXACT code snippets to change.

---

## FIGURE 1: Combine Spatial + Timeseries Panels c,d

### Setup
1. Create new notebook: `figure_01_spatial_and_timeseries.ipynb`
2. Copy **Cell 1** from original (spatial maps) - I've provided this complete in `fig1_cell1_spatial.py`
3. For timeseries (panels c,d), use original Cell 2 but with modifications below

### Cell 2 Modifications for Figure 1

#### At the top, change figure layout:
```python
# REPLACE THIS:
fig = plt.figure(figsize=(12, 10))
gs = fig.add_gridspec(3, 2, hspace=0.2, wspace=0.15, 
                      left=0.08, right=0.98, top=0.98, bottom=0.05)

axes = []
for i in range(3):
    for j in range(2):
        ax = fig.add_subplot(gs[i, j])
        axes.append(ax)

# WITH THIS:
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
axes = axes.flatten()

# First two axes are for spatial maps (already done in Cell 1)
# So we'll use axes[2] and axes[3] for timeseries
```

#### Find Panel (a) - Pan-Arctic (line ~1222) and change:
```python
# CHANGE:
ax = axes[0]
# TO:
ax = axes[2]  # Third panel in 2x2 grid

# CHANGE title from:
ax.set_title('a) Pan-Arctic', ...)
# TO:
ax.set_title('c) Pan-Arctic, split linear trends', ...)
```

#### Find Panel (b) - Greenland Sea (line ~1314) and change:
```python
# CHANGE:
ax = axes[1]
# TO:
ax = axes[3]  # Fourth panel in 2x2 grid

# CHANGE title from:
ax.set_title('b) Greenland Sea', ...)
# TO:
ax.set_title('d) Greenland Sea, split linear trends', ...)
```

#### RED SQUARES for Greenland Sea max years (in Panel d section, around line 1380):
Find where it marks the maximum extent years:
```python
# FIND this code block (should be inside the Greenland Sea panel loop):
for year in [1986, 2023]:  # Or similar years
    year_data = y_data.where(x_data.dt.year == year, drop=True)
    if len(year_data) > 0:
        year_time = x_data.where(x_data.dt.year == year, drop=True).values[0]
        ax.scatter(year_time, year_data.values[0], s=120, marker='s',
                  color=COLOR_MOORING, edgecolors='white', linewidth=1.5,  # OLD
                  zorder=5, alpha=0.8)

# CHANGE TO:
        ax.scatter(year_time, year_data.values[0], s=120, marker='s',
                  color='red', edgecolors='none',  # NEW - simple red squares
                  zorder=5, alpha=0.8)
```

#### REMOVE panels c, d, e, f (PWLR and SSA sections):
Delete everything after Panel (b) Greenland Sea split trends ends.
This includes:
- Lines ~1404-1608 (all of ROW 2 and ROW 3)
- Keep only the save/show code at the end

#### Update output path (near end):
```python
# CHANGE:
output_path = f"{output_dir}/Fig2_SIE_trends_winter_6panel_CI.png"
# TO:
output_path = "./outputs/figures/figure_01.png"
```

---

## FIGURE S1: Piecewise + SSA (panels a,b,c,d)

### Setup
1. Create new notebook: `figure_s1_piecewise_and_ssa.ipynb`
2. Copy from original Cell 2 (timeseries)

### Modifications

#### Keep only these sections from Cell 2:
- Imports and CONFIG
- All function definitions (mann_kendall through perform_ssa_analysis)
- OSISAF data loading
- Panel (c) PWLR Arctic → becomes Panel (a)
- Panel (d) PWLR Greenland → becomes Panel (b)
- Panel (e) SSA Arctic → becomes Panel (c)
- Panel (f) SSA Greenland → becomes Panel (d)

#### Change figure layout:
```python
# REPLACE 6-panel layout with:
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()
```

#### Update panel indexing and titles:

**PWLR Arctic** (was Panel c, line ~1404):
```python
# CHANGE:
ax = axes[2]
print(f"\nPanel (c): Pan-Arctic {season_name} PWLR")
# TO:
ax = axes[0]
print(f"\nPanel (a): Pan-Arctic {season_name} PWLR")

# Title change:
ax.set_title('a) Pan-Arctic, piecewise linear regression', loc='left')
```

**PWLR Greenland** (was Panel d, line ~1446):
```python
# CHANGE:
ax = axes[3]
print(f"\nPanel (d): Greenland Sea {season_name} PWLR")
# TO:
ax = axes[1]
print(f"\nPanel (b): Greenland Sea {season_name} PWLR")

# Title change:
ax.set_title('b) Greenland Sea, piecewise linear regression', loc='left')
```

**SSA Arctic** (was Panel e, line ~1510):
```python
# CHANGE:
ax = axes[4]
print(f"\nPanel (e): Pan-Arctic {season_name} SSA")
# TO:
ax = axes[2]
print(f"\nPanel (c): Pan-Arctic {season_name} SSA")

# Title change:
ax.set_title('c) Pan-Arctic, SSA decomposition', loc='left')
```

**SSA Greenland** (was Panel f, line ~1560):
```python
# CHANGE:
ax = axes[5]
print(f"\nPanel (f): Greenland Sea {season_name} SSA")
# TO:
ax = axes[3]
print(f"\nPanel (d): Greenland Sea {season_name} SSA")

# Title change:
ax.set_title('d) Greenland Sea, SSA decomposition', loc='left')
```

#### Output path:
```python
output_path = "./outputs/figures/figure_s1.png"
```

---

## Quick Checklist

### Figure 1:
- [ ] Use complete `fig1_cell1_spatial.py` as Cell 1
- [ ] Cell 2 uses axes[2] and axes[3] for panels c,d
- [ ] Red squares (not purple) for Greenland Sea max years
- [ ] Output: `./outputs/figures/figure_01.png`
- [ ] Remove all PWLR and SSA code

### Figure S1:
- [ ] 2x2 grid, axes[0-3]
- [ ] Only PWLR and SSA panels
- [ ] Panel labels a,b,c,d
- [ ] Output: `./outputs/figures/figure_s1.png`
- [ ] Remove split trend panels code

---

## Files Provided

1. **fig1_cell1_spatial.py** - Complete Cell 1 for Figure 1 (spatial maps with all modifications)
2. This guide - Exact snippets for Cell 2 modifications

Simply copy the original notebook twice, apply these changes, and you're done!
