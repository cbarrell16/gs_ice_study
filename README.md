# Greenland Sea Ice Study

Analysis code for the manuscript *"Reversal of wintertime sea-ice decline in the
Greenland Sea despite record low pan-Arctic extents"*, submitted to
*Nature Communications*.

Wintertime sea-ice extent in the Greenland Sea has increased since 2015, reversing
its earlier decline during a period of record-low pan-Arctic extents. The analysis
shows a transition from pre-2015 Atlantification to post-2015 freshening by an
increased and fresher Polar Surface Water inflow through Fram Strait, which
strengthens upper-ocean stratification. This acts together with stronger
early-winter cold-air outbreaks linked to large-scale atmospheric circulation.

## Project structure

```
gs_ice_study/
├── config.yaml              # Central configuration (data paths, parameters, plotting)
├── environment.yml          # Conda environment specification
├── data_README.md           # Documentation of all external data sources
├── utils/                   # Shared logging utilities (logger.py)
└── notebooks/               # Analysis notebooks (see table below)
    └── outputs/             # Created when notebooks run; not tracked in Git
        ├── figures/         # Publication figures (600 DPI PNG)
        ├── processed_data/  # Intermediate NetCDF/CSV used for replotting
        ├── methods/         # Auto-generated methods documentation
        └── logs/            # Processing logs
```

Subdirectories of `notebooks/` (including all outputs) are excluded from Git.
Processed data needed for replotting will be archived on Zenodo.

## Notebooks and run order

| Step | Notebook | Produces |
|---|---|---|
| 1. Data preparation | `download_preprocess_glorys12_nordic_seas.ipynb` | GLORYS12 subset with density |
| | `osisaf_sii_v3_download.ipynb` | OSI SAF sea-ice extent (daily and monthly) |
| | `climate_indices_download.ipynb` | Climate indices (NAO, AO, GBI, SCAND, NINO3.4, TPQD, PDO) |
| | `compute_arctic_dipole.ipynb` | Arctic Dipole index from ERA5 |
| | `argo_glorys_pairing.ipynb` | Argo–GLORYS12 collocated profiles |
| 2. Main figures | `figure_01_SIE_timeseries_and_SIC_spatial_trends.ipynb` | Fig. 1 |
| | `figure_02_SIV_decomposition.ipynb` | Fig. 2 |
| | `figure_03_Greenland_Sea_T_and_S.ipynb` | Fig. 3 |
| | `figure_04_PSW_and_AW.ipynb` | Fig. 4 |
| | `figure_05_PSW_extent.ipynb` | Fig. 5 |
| | `figure_06_CAOidx_SEB.ipynb` | Fig. 6 (also writes the CAO index used in Fig. 8) |
| | `figure_07_atmospheric_composites.ipynb` | Fig. 7 |
| 3. Correlations | `compute_monthly_ondjfma_correlations.ipynb` | Unfiltered correlations |
| | `compute_trimmed_correlation_matrix.ipynb` | Band-pass filtered correlations and significance |
| | `figure_08_correlation_and_phases_combined.ipynb` | Fig. 8 |
| 4. Supplementary figures | `figure_s01_glorys12_sea_ice_verification.ipynb` | Fig. S1 |
| | `figure_s02_GLORYS12_T_S_verification.ipynb` | Fig. S2 |
| | `figure_s03_FS_mooring_glorys_verification.ipynb` | Fig. S3 |
| | `figure_s04_FS_FWT_GLORYS12_verification.ipynb` | Fig. S4 |
| | `figures_s05_s06_observing_network_sensitivity_and_trend_fidelity.ipynb` | Figs S5 and S6 |
| Other (not required for the paper figures) | `Equations.ipynb` | Rendered equations for the Methods |
| | `figure_02_spatial_diagnostics.ipynb` | Diagnostic maps supporting Fig. 2 |
| | `figure_03_Greenland_Sea_T_and_S_original.ipynb` | Earlier version of Fig. 3 |

## Setup

### 1. Create conda environment

```bash
conda env create -f environment.yml
conda activate gs_ice_study
```

### 2. Configure data paths

Data files are stored outside the repository. Default paths in `config.yaml`
assume data is two levels up from the `notebooks/` directory:
- ERA5: `../../era5/`
- OSI SAF: `../../osi-sea_ice_index/`
- GLORYS12: `../../glorys12_with_density/`

Edit `config.yaml` (and the path constants at the top of each notebook) if your
data is stored elsewhere.

### 3. Run notebooks

```bash
jupyter lab
```

Run the notebooks in the order given above. Each notebook produces its own
figures, processed data and methods documentation in `notebooks/outputs/`.

## Reprocessing vs. replotting

Each notebook has a `REPROCESS` flag near the top:

- **`REPROCESS = True`** loads the raw source data, recomputes all processed
  outputs and saves them to `notebooks/outputs/processed_data/`. This requires
  access to the full external datasets.
- **`REPROCESS = False`** (default) loads previously saved processed data only,
  for replotting without the raw data. Download the processed data from Zenodo
  into `notebooks/outputs/processed_data/` first.

## Configuration

All key parameters are centralised in `config.yaml`:
- Greenland Sea breakpoint year: **2015** (identified by piecewise linear regression)
- Pan-Arctic breakpoint year: **2017** (set per notebook as `BREAK_YEAR_NH`)
- Winter: October–April (early winter ONDJ, late winter FMA), labelled by the year of January
- Bootstrap iterations: **1000**; confidence level: **0.95**

## Data sources

See `data_README.md` for full documentation of:
- ERA5 atmospheric reanalysis (ECMWF)
- OSI SAF Sea Ice Index (daily and monthly products)
- GLORYS12 ocean reanalysis (Copernicus Marine Service)
- Fram Strait Arctic Outflow Observatory mooring records (Norwegian Polar Institute)
- Argo float profiles (Argo GDAC)
- IGP 2018 field campaign CTD/XCTD profiles
- ROVER 2025 field campaign CTD profiles

## Citation

This repository will be archived with a DOI via Zenodo.

## License

To be determined upon publication.

## Contact

Chris Barrell (c.barrell@uea.ac.uk)
School of Environmental Sciences, University of East Anglia, Norwich, UK
