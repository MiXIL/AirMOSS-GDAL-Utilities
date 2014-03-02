AirMOSS GDAL Utilities
======================

Set of utility scripts for converting and working with AirMOSS data and retrievals using GDAL

The scripts require Python with NumPy, H5Py and GDAL (Python bindings).

### Conversion ###

* convertAirMOSS2GDAL.py - Convert AirMOSS data (H5 format) to GDAL

* convertAirMOSSRetrieval2GDAL - Convert USC AirMOSS soil moisture retreval to GDAL

### Retreval Utilities ###

* airmoss_gen_sm.py - Generate image with soil moisture retreval at a range of depths for visualising profile in TuiView. Requires RIOS.
