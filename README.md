# Greenland Sea Ice Study

Analysis of wintertime sea-ice recovery in the Greenland Sea, investigating
a two-phase regime transition around 2015: pre-2015 Atlantification followed
by post-2015 Polar Surface Water freshening and regional sea-ice recovery —
occurring paradoxically during a period of record-low pan-Arctic extents.

This repository contains the analysis code for the manuscript submitted to
*Nature Climate Change*.

## Project Structure

```
gs_ice_study/
├── config.yaml              # Central configuration file
├── environment.yml          # Conda environment specification
├── data_README.md           # Documentation of all external data sources
├── utils/                   # Shared utility functions
│   ├── __init__.py
│   ├── logger.py            # Logging configuration
│   ├── data_utils.py        # Data loading and processing
│   ├── stats_utils.py       # Statistical analysis functions
│   └── plot_utils.py        # Plotting utilities and styling
├── notebooks/               # Analysis notebooks, one per figure
│   ├── figure_01_SIE_timeseries_and_SIC_spatial_trends.ipynb
│   └── ...
└── outputs/                 # All outputs (not in Git except processed_data)
    ├── figures/             # Final publication figures (600 DPI PNG)
    ├── processed_data/      # Intermediate NetCDF/CSV files for replotting
    ├── logs/                # Processing logs (not in Git)
    └── methods/             # Auto-generated methodology documentation
```

## Setup

### 1. Create conda environment

```bash
conda env create -f environment.yml
conda activate gs_ice_study
```

### 2. Configure data paths

Data files are stored outside the repository. Default paths in `config.yaml`
assume data is two levels up from the project root:
- ERA5: `../../era5/`
- OSISAF: `../../osi-sea_ice_index/`
- GLORYS12: `../../glorys12_with_density/`

Edit `config.yaml` if your data is stored elsewhere.

### 3. Run notebooks

```bash
jupyter lab
```

Navigate to `notebooks/` and run the analysis notebooks. Each notebook is
self-contained and produces its own figures, processed data, and methods
documentation.

## Configuration

All parameters are centralised in `config.yaml`:
- **Data paths**: source data locations
- **Analysis parameters**: breakpoint years, confidence levels, thresholds
- **Plotting settings**: colours, DPI, figure sizes
- **Units**: consistent units across all outputs

Key parameters:
- Greenland Sea breakpoint year: **2015** (confirmed by piecewise linear regression)
- Pan-Arctic breakpoint year: **2017** (set per-script as `BREAK_YEAR_NH`)
- Bootstrap iterations: **1000**
- Confidence level: **0.95**

## Reprocessing vs. Replotting

Each notebook has a `REPROCESS` flag near the top of the script:

- **`REPROCESS = True`**: loads all raw source data, recomputes all processed
  outputs (NetCDF/CSV files), and saves them to `outputs/processed_data/figure_XX/`.
  Requires access to the full external datasets.
- **`REPROCESS = False`** (default): loads from previously saved processed data
  only. Suitable for replotting figures without access to raw data.

Run each notebook once with `REPROCESS = True` to generate the processed data
cache, then subsequent runs with `REPROCESS = False` are fast and self-contained.

## Outputs

### Figures
Publication-quality figures saved to `outputs/figures/` at 600 DPI.

### Processed Data
Intermediate NetCDF and CSV files in `outputs/processed_data/figure_XX/`
allow replotting without reprocessing raw data (see `REPROCESS` flag above).

### Logs
Detailed processing logs in `outputs/logs/` (excluded from Git). Each run
produces a timestamped log with data sources, processing steps, and outputs.

### Methods Documentation
Auto-generated Markdown files in `outputs/methods/` document data sources,
mathematical formulations, and statistical methods for each figure.

## Data Sources

See `data_README.md` for full documentation of:
- ERA5 atmospheric reanalysis (ECMWF)
- OSISAF Sea Ice Index (daily and monthly products)
- GLORYS12 ocean reanalysis (Copernicus Marine Service)
- Fram Strait mooring records (Norwegian Polar Institute)
- Argo float profiles (Argo GDAC)
- IGP 2018 field campaign CTD/XCTD profiles
- ROVER 2025 field campaign CTD profiles

## Reproducibility

To execute all notebooks in order:

```bash
jupyter nbconvert --execute --to notebook --inplace notebooks/figure_01_SIE_timeseries_and_SIC_spatial_trends.ipynb
# ... repeat for each figure notebook
```

## Citation

When published, this repository will be archived with a DOI via Zenodo.

## License

To be determined upon publication.

## Contact

Chris Barrell (c.barrell@uea.ac.uk)
School of Environmental Sciences
University of East Anglia
Norwich, UK
