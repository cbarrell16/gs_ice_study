# Data Sources

This document describes all external data sources used in this analysis.
Data files are stored outside the Git repository. See `config.yaml` for
the canonical path to each dataset.

## Directory Structure

Data is expected in the following locations relative to the `notebooks/` directory
(some field and mooring datasets are currently set as absolute paths at the top of
the relevant notebooks; edit these to match your system):

```
../../era5/                        # ERA5 atmospheric reanalysis
../../osi-sea_ice_index/           # OSISAF sea ice index
../../glorys12_with_density/       # GLORYS12 ocean reanalysis (with pre-computed density)
../../from_laura/                  # Fram Strait Arctic Outflow Observatory (NPI) data
../../climate_indices/raw/         # Climate index source files
IGP_data/                          # Iceland Greenland Seas Project data (IGP2018)
KH_CTD/                            # ROVER winter campaign CTD data (KH2025)
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
**Variables**: Sea-ice extent (daily and monthly, OSI-420)
**Temporal coverage**: 1979–present
**Regions**: Northern Hemisphere (`nh`), Greenland Sea/Fram Strait (`fram`)
**Files**: `../../osi-sea_ice_index/*`

**Citation**:
EUMETSAT OSI SAF. Sea-Ice Index, OSI-420. https://doi.org/10.15770/EUM_SAF_OSI_0026

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

### Fram Strait Arctic Outflow Observatory (FSAOO) moorings

**Source**: Norwegian Polar Institute (NPI)
**Contact**: Laura de Steur (laura.de.steur@npolar.no)
**Variables**: Temperature, salinity, velocity; derived freshwater transport (2002–2024)
and sea-ice volume export (1990–2020)
**Temporal coverage**: Variable by mooring (western Fram Strait array, F11–F17)
**Mooring latitude**: ~78.8°N
**Mooring longitudes**: F10 (−2.0°E), F11 (−3.0°E), F12 (−4.0°E),
  F13 (−5.0°E), F13b (−5.5°E), F14 (−6.5°E), F17 (−8.0°E)
**Files**: `../../from_laura/*`

**Notes**: Gaps in some moorings handled via data coverage thresholds.

**Citation**:
de Steur, L. (2021). Moored current meter and hydrographic data from the Fram Strait
Arctic Outflow Observatory since 2009. Norwegian Polar Institute.
https://doi.org/10.21334/NPOLAR.2021.C4D80B64

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
**Files**: `IGP_data/*`

**Notes**: Available from Woods Hole Oceanographic Institution
(https://web.whoi.edu/all0118/).

**Citation**:
Renfrew, I. A. et al. (2019). The Iceland Greenland Seas Project. *Bulletin of the
American Meteorological Society*, 100, 1795–1817.

---

### ROVER Winter Field Campaign — 2025 (KH2025)

**Source**: ROVER winter campaign on RV Kronprins Haakon (February–March 2025)
**Variables**: CTD hydrographic profiles
**Files**: `KH_CTD/*`

**Notes**: Being archived at the Norwegian Marine Data Centre (NMDC); will be
publicly available by the time of publication.

---

### Sea-ice drift and thickness (verification only, Fig. S1)

- **Drift**: EUMETSAT OSI SAF OSI-455 (1991–2020, https://doi.org/10.15770/EUM_SAF_OSI_0012)
  and OSI-405-d (2021 onwards, https://doi.org/10.15770/EUM_SAF_OSI_NRT_2007).
  Known issues handled in processing: historical sign error in u/v drift components
  (u corrected throughout; v corrected for December 2009–May 2015); date-based split
  at 2021-01-01 to avoid double-counting the product overlap.
- **Thickness**: Copernicus Climate Change Service gridded Arctic sea-ice thickness
  (CryoSat-2, 2010–2024, October–April), https://doi.org/10.24381/cds.6679a99a

---

### Climate indices

**Source**: NOAA Physical Sciences Laboratory
(https://psl.noaa.gov/data/climateindices/list/): GBI, NAO, SCAND, AO, NINO3.4,
NINO4, PDO.
**Derived in this repository**: TPQD (9–16-year Butterworth band-pass of NINO4,
following Xu et al. 2026) and the Arctic Dipole (second EOF of ERA5 sea-level
pressure north of 70°N, following Wu et al. 2006).
**Files**: `../../climate_indices/raw/`

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
- GLORYS12 analysis period: 1993–April 2026
- OSISAF timeseries period: 1979–April 2026
- Breakpoint: 2015 (Period 1: before 2015; Period 2: 2015 onwards)

### Water Mass Definitions

- **Polar Surface Water (PSW)**: S < 34.5 psu AND ρ < 1027.7 kg m⁻³
- **Atlantic Water (AW)**: lon > 5°E, depth < 550 m (eastern diagonal boundary)
- All TEOS-10 conversions applied using `gsw` package

## Data Size

Approximate storage requirements (not in Git):
- ERA5: ~50 GB (Arctic subset, 1979–2025)
- GLORYS12: ~200 GB (regional subset, monthly, with density fields)
- OSISAF: ~5 GB
- Fram Strait moorings: ~500 MB
- Argo: downloaded on-demand via API
- IGP and KH2025: ~100 MB

Total: ~256 GB external data

## Reproducibility

1. Request access to GLORYS12 and ERA5 via Copernicus Marine/Climate Services
2. Download OSISAF data from https://osi-saf.eumetsat.int/
3. Contact mooring data providers for Fram Strait records
4. Argo data accessed automatically via `argopy`
5. IGP data from WHOI; KH2025 data from NMDC (once released)
6. ETOPO1 downloaded automatically via `rockhound`

Adjust paths in `config.yaml` if your directory structure differs from above.
