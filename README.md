# Greenland Sea Ice Study

Analysis of Greenland Sea ice dynamics, ocean-atmosphere interactions, and water mass transformations.

## Project Structure

```
gs_ice_study/
├── config.yaml              # Central configuration file
├── environment.yml          # Conda environment specification
├── utils/                   # Shared utility functions
│   ├── data_utils.py       # Data loading and processing
│   ├── stats_utils.py      # Statistical analysis functions
│   ├── plot_utils.py       # Plotting utilities and styling
│   └── logger.py           # Logging configuration
├── notebooks/               # Analysis notebooks for each figure
│   ├── figure_01.ipynb
│   └── ...
├── outputs/                 # All outputs organized by type
│   ├── figures/            # Final publication figures
│   ├── processed_data/     # Intermediate data files (.nc)
│   ├── logs/               # Processing logs (not in Git)
│   └── methods/            # Auto-generated methodology docs
└── data/                    # Reference only (actual data stored externally)
    └── README.md           # Documentation of data sources
```

## Setup

### 1. Create conda environment

```bash
conda env create -f environment.yml
conda activate gs_ice_study
```

### 2. Configure paths

Edit `config.yaml` to point to your data directories. Default paths assume data is in parent directory:
- ERA5: `../era5/`
- OSISAF: `../osi-sea_ice_index/`

### 3. Run notebooks

```bash
jupyter lab
```

Navigate to `notebooks/` and run the analysis notebooks in order.

## Configuration

All parameters are centralized in `config.yaml`:
- **Data paths**: Source data locations
- **Analysis parameters**: Breakpoint years, confidence levels, thresholds
- **Plotting settings**: Colors, DPI, figure sizes
- **Units**: Consistent units across all outputs

Edit this file to change parameters globally across all analyses.

## Outputs

### Figures
Publication-quality figures saved to `outputs/figures/` at 600 DPI.

### Processed Data
Intermediate NetCDF files saved to `outputs/processed_data/` for:
- Quick re-plotting without reprocessing
- Verification and validation
- Sharing processed datasets

Each notebook can be configured to use cached data via `config.yaml`:
```yaml
processing:
  use_cached_data: true  # Use existing processed data
```

### Logs
Detailed processing logs in `outputs/logs/` include:
- Timestamp and execution time
- Data sources accessed
- Processing steps executed
- Warnings and errors
- Output files created

### Methods Documentation
Auto-generated methodology descriptions in `outputs/methods/` document:
- Data sources and processing
- Statistical methods with references
- Figure-specific analysis details

Use these as a starting point for manuscript methods sections.

## Data Sources

See `data/README.md` for detailed documentation of:
- ERA5 atmospheric reanalysis
- OSISAF sea ice products
- Fram Strait mooring data
- Argo float observations
- IGP field campaign data

## Reproducibility

To reproduce all figures:

```bash
# From project root
jupyter nbconvert --execute --to notebook --inplace notebooks/figure_01.ipynb
jupyter nbconvert --execute --to notebook --inplace notebooks/figure_02.ipynb
# ... etc
```

Or use the provided script (when created):
```bash
python run_all_analyses.py
```

## Citation

When published, this repository will be made public with DOI via Zenodo.

## License

Private repository - to be determined upon publication.

## Contact

[Your contact information]

## Version

Current version: 1.0.0-dev
Last updated: 2026-02-27
