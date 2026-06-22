# Data Sources

This document describes all external data sources used in this analysis.
Data files are stored outside the Git repository. See `config.yaml` for
the canonical path to each dataset.

## Directory Structure

Data is expected in the following locations relative to the project root:

```
../../era5/                        # ERA5 atmospheric reanalysis
../../osi-sea_ice_index/           # OSISAF sea ice index
../../glorys12_with_density/       # GLORYS12 ocean reanalysis (with pre-computed density)
../../fram_strait_moorings/        # Fram Strait mooring observations
../../argo/                        # Argo float profiles
../../igp/                         # Iceland Greenland Seas Project data
```

## Data Products

### ERA5 Atmospheric Reanalysis

**Source**: ECMWF ERA5
**Variables**: Sea ice concentration (`siconc`), atmospheric fields
**Temporal coverage**: 1979–present
**Spatial resolution**: 0.25° × 0.25°
**Files**: `../../era5/era5_*_Arctic.nc`

**Citation**:
Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A.,
Muñoz-Sabater, J., ... & Thépaut, J.-N. (2020). The ERA5 global reanalysis.
*Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999–2049.
https://doi.org/10.1002/qj.3803

**Access**: https://cds.climate.copernicus.eu/

---

### OSISAF Sea Ice Index

**Source**: Ocean and Sea Ice Satellite Application Facility (OSI SAF)
**Variables**: Sea ice extent, area, concentration (daily and monthly)
**Temporal coverage**: 1979–present
**Regions**: Northern Hemisphere (`nh`), Greenland Sea/Fram Strait (`fram`)
**Files**: `../../osi-sea_ice_index/*`

**Known data issues (handled in processing)**:
- Historical sign error in u/v drift components: u-component corrected
  throughout; v-component corrected for December 2009–May 2015.
- OSI-455/OSI-405 product overlap: date-based split applied at 2021-01-01
  in scatter plots to avoid double-counting.

**Citation**:
OSI SAF (2017). Global Sea Ice Concentration Climate Data Record v2.0 —
Multimission. EUMETSAT SAF on Ocean and Sea Ice.
https://osi-saf.eumetsat.int/

**Access**: https://osi-saf.eumetsat.int/

---

### GLORYS12 Ocean Reanalysis

**Source**: Copernicus Marine Service
**Variables**: Temperature, salinity, velocity, sea surface height
**Temporal coverage**: 1993–present
**Spatial resolution**: 1/12° (~8 km)
**Files**: `../../glorys12_with_density/glorys12_*_Greenland_Sea_with_density.nc`

**Notes**: Files include pre-computed Absolute Salinity (SA), Conservative
Temperature (CT), in-situ temperature, and potential density (sigma0) via
the TEOS-10 pipeline (gsw package). Parallel loading must be disabled
(`parallel=False` with `xr.open_mfdataset`) to avoid kernel crashes.

**Citation**:
Lellouche, J.-M., Greiner, E., Le Galloudec, O., Garric, G., Regnier, C.,
Drevillon, M., ... & Le Traon, P.-Y. (2021). The Copernicus Global 1/12°
Oceanic and Sea Ice GLORYS12 Reanalysis. *Frontiers in Earth Science*, 9,
698876. https://doi.org/10.3389/feart.2021.698876

**Access**: https://marine.copernicus.eu/

---

### Fram Strait Moorings

**Source**: Norwegian Polar Institute (NPI)
**Contact**: Laura de Steur (laura.de.steur@npolar.no)
**Variables**: Temperature, salinity, velocity
**Temporal coverage**: Variable by mooring (eastern array F11–F17)
**Mooring latitude**: 79°N
**Mooring longitudes**: F10 (−2.0°E), F11 (−3.0°E), F12 (−4.0°E),
  F13 (−5.0°E), F13b (−5.5°E), F14 (−6.5°E), F17 (−8.0°E)
**Files**: `../../fram_strait_moorings/*`

**Notes**: Gaps in some moorings handled via data coverage thresholds.
Contact data provider for access.

**Access**: Contact data providers directly.

---

### Argo Float Profiles

**Source**: Argo Program / Argo GDAC
**Variables**: Temperature and salinity profiles
**Temporal coverage**: 2000–present
**Region**: Greenland Sea (subset)
**Access method**: `argopy` Python package with `erddap` source

**Citation**:
Argo (2000). Argo float data and metadata from Global Data Assembly Centre
(Argo GDAC). SEANOE. https://doi.org/10.17882/42182

**Access**: https://argo.ucsd.edu/

---

### Iceland Greenland Seas Project (IGP) — 2018 Field Campaign

**Source**: 2018 field campaign (February–March 2018)
**Variables**: CTD and XCTD hydrographic profiles
**Temporal coverage**: February–March 2018
**Storage**: WHOI FTP servers
**Files**: `../../igp/*`

**Notes**: Manual download required from FTP servers. Campaign participation
grants usage rights. Contact authors for FTP access details.

---

### ETOPO1 Bathymetry

**Source**: NOAA National Centers for Environmental Information
**Variables**: Global relief model (ice surface)
**Access method**: `rockhound.fetch_etopo1(version="ice")`

**Citation**:
Amante, C., & Eakins, B. W. (2009). ETOPO1 1 Arc-Minute Global Relief Model:
Procedures, Data Sources and Analysis. NOAA Technical Memorandum NESDIS
NGDC-24. https://doi.org/10.7289/V5C8276M

---

## Data Processing Notes

### Quality Control

- ERA5 and GLORYS12: pre-validated by data providers
- OSISAF: standard quality flags applied; known sign errors corrected
- Mooring data: gaps handled via coverage thresholds
- Argo: standard Argo QC flags respected
- IGP: manual validation during field campaign

### Temporal Conventions

- All data aggregated to monthly resolution where applicable
- Complete seasons only (incomplete seasons filtered by month count)
- Winter seasons labelled by year of January (ONDJ convention)
- GLORYS12 analysis period: 1993–2025 (data availability)
- OSISAF timeseries period: 1979–2025

### Water Mass Definitions

- **Polar Surface Water (PSW)**: S < 34.5 psu AND σ₀ < 1027.7 kg m⁻³
- **Atlantic Water (AW)**: lon > 5°E, depth < 550 m (eastern diagonal boundary)
- All TEOS-10 conversions applied using `gsw` package

## Data Size

Approximate storage requirements (not in Git):
- ERA5: ~50 GB (Arctic subset, 1979–2025)
- GLORYS12: ~200 GB (regional subset, monthly, with density fields)
- OSISAF: ~5 GB
- Fram Strait moorings: ~500 MB
- Argo: downloaded on-demand via API
- IGP: ~100 MB

Total: ~256 GB external data

## Reproducibility

1. Request access to GLORYS12 and ERA5 via Copernicus Marine/Climate Services
2. Download OSISAF data from https://osi-saf.eumetsat.int/
3. Contact mooring data providers for Fram Strait records
4. Argo data accessed automatically via `argopy`
5. IGP data: contact authors for FTP access
6. ETOPO1 downloaded automatically via `rockhound`

Adjust paths in `config.yaml` if your directory structure differs from above.
