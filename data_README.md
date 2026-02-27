# Data Sources

This document describes all external data sources used in this analysis. The actual data files are stored in parent directories (`../`) and are not included in this Git repository.

## Directory Structure

Data is expected in the following locations relative to the project root:

```
../era5/                     # ERA5 atmospheric reanalysis
../osi-sea_ice_index/        # OSISAF sea ice index
../glorys/                   # GLORYS12 ocean reanalysis
../fram_strait_moorings/     # Fram Strait mooring observations
../argo/                     # Argo float profiles
../igp/                      # Iceland Greenland Seas Project data
```

## Data Products

### ERA5 Atmospheric Reanalysis

**Source**: ECMWF ERA5  
**Variables**: Sea ice concentration (`siconc`), atmospheric fields  
**Temporal coverage**: 1979-present  
**Spatial resolution**: 0.25° × 0.25°  
**Files**: `../era5/era5_*_Arctic.nc`

**Citation**:
Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.

**Access**: https://cds.climate.copernicus.eu/

### OSISAF Sea Ice Index

**Source**: Ocean and Sea Ice Satellite Application Facility  
**Variables**: Sea ice extent, area, concentration  
**Temporal coverage**: 1979-present  
**Regions**: Northern Hemisphere, regional seas  
**Files**: `../osi-sea_ice_index/*`

**Citation**:
OSI SAF (2017). Global Sea Ice Concentration Climate Data Record v2.0 - Multimission. EUMETSAT SAF on Ocean and Sea Ice.

**Access**: https://osi-saf.eumetsat.int/

### GLORYS12 Ocean Reanalysis

**Source**: Copernicus Marine Service  
**Variables**: Temperature, salinity, velocity, SSH  
**Temporal coverage**: 1993-present  
**Spatial resolution**: 1/12° (~8 km)  
**Files**: `../glorys/GLORYS12*.nc`

**Citation**:
Lellouche, J.-M., et al. (2021). The Copernicus Global 1/12° Oceanic and Sea Ice GLORYS12 Reanalysis. *Frontiers in Earth Science*, 9, 698876.

**Access**: https://marine.copernicus.eu/

### Fram Strait Moorings

**Source**: Alfred Wegener Institute (AWI) / Norwegian Polar Institute  
**Contact**: Laura de Steur  
**Variables**: Temperature, salinity, velocity  
**Temporal coverage**: Variable by mooring  
**Locations**: F10-F17 array across Fram Strait  
**Files**: `../fram_strait_moorings/*`

**Citation**:
de Steur, L., et al. (2014). Recent changes in the Fram Strait oceanic fluxes. *Ocean Science*, 10(4), 611-622.

**Access**: Contact data providers directly

### Argo Float Profiles

**Source**: Argo Program  
**Variables**: Temperature, salinity profiles  
**Temporal coverage**: 2000-present  
**Region**: Greenland Sea (subset)  
**Access method**: `argopy` package with erddap source

**Citation**:
Argo (2000). Argo float data and metadata from Global Data Assembly Centre (Argo GDAC). SEANOE. https://doi.org/10.17882/42182

**Access**: https://argo.ucsd.edu/

### Iceland Greenland Seas Project (IGP)

**Source**: 2018 field campaign  
**Variables**: CTD and XCTD profiles  
**Temporal coverage**: 2018  
**Storage**: WHOI FTP servers  
**Files**: `../igp/*`

**Notes**: Manual download required from FTP servers. Campaign participation grants usage rights.

## Data Processing Notes

### Quality Control

All data sources undergo quality control:
- ERA5 and GLORYS: Pre-validated by data providers
- OSISAF: Standard quality flags applied
- Mooring data: Systematic corrections for velocity sign errors and temporal gaps
- Argo: Standard Argo QC flags respected
- IGP: Manual validation during field campaign

### Temporal Alignment

- Monthly mean fields: All data aggregated to monthly resolution
- Seasonal analysis: Complete seasons only (filter incomplete years)
- Coordinate consistency: All datasets verified for coordinate compatibility

### Known Issues

1. **OSISAF velocity data**: Historical sign error in u/v components (corrected in processing)
2. **Mooring temporal coverage**: Gaps in some moorings require careful data coverage thresholds
3. **ERA5 time coordinates**: Inconsistent time coordinate across some files (handled during loading)

## Data Size

Approximate data storage requirements:
- ERA5: ~50 GB (Arctic subset, 1979-2025)
- GLORYS12: ~200 GB (regional subset, monthly)
- OSISAF: ~5 GB
- Moorings: ~500 MB
- Argo: Downloaded on-demand via API
- IGP: ~100 MB

Total: ~255 GB external data (not in Git)

## Reproducibility

To reproduce this analysis:

1. Request access to GLORYS12 and ERA5 via Copernicus
2. Download OSISAF data from their portal
3. Contact mooring data providers for access
4. Argo data accessed automatically via `argopy`
5. IGP data: Contact authors for FTP access

All processing scripts assume the directory structure above. Adjust paths in `config.yaml` if needed.

## Updates

Last verified: 2026-02-27  
Next update: When new data becomes available
