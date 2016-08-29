AirMOSS GDAL Utilities
======================

A set of utility scripts for converting and working with H5 format AirMOSS data and retrievals using GDAL, allowing them to be used in popular GIS packages (e.g., QGIS, ArcMap).

The conversion scripts require Python with NumPy, H5Py and GDAL (Python bindings). If you don't already have these installed you can download Anaconda / Miniconda from https://store.continuum.io/cshop/anaconda/

Once installed use:

    conda install -c conda-forge h5py gdal rios

to install the required libraries. You may also with to install `tuiview` to view the exported files.

### Conversion ###

* **convertAirMOSS2GDAL.py** - Convert AirMOSS data (H5 format) to GDAL.
Usage:
```
python convertAirMOSS2GDAL.py -i AirMOSS.h5 -o AirMOSS.tif
```

* **convertAirMOSSRetrieval2GDAL.py** - Convert USC AirMOSS soil moisture retreval to GDAL.
Usage:
```
python convertAirMOSSRetrieval2GDAL.py -i AirMOSS_retreval.h5 -o AirMOSS_retreval.tif
```
To export as gamma0 (sigma0 / cos(theta)) pass in `--gamma0`. To export values in dB pass in `--dB`.

### Retreval Utilities ###

* **airmoss_gen_sm.py** - Generate image with soil moisture retrieval at a range of depths for visualising profile in TuiView / ENVI. 
Usage:
```
python airmoss_gen_sm.py -i AirMOSS_retreval.tif -o AirMOSS_retreval_0_100cm.tif
```

* **colour_sm_image.py** - Colour soil moisture image and export as a three band RGB image, can optionally export as KMZ file.
This also requires RSGISLib, currently only available on macOS and Linux. To install use:
```
conda install -c conda-forge -c osgeo rsgislib
```

Usage:
```
python colour_sm_image.py -i AirMOSS_retreval_0_100cm.tif \
                          -o AirMOSS_retreval_5cm_col.tif \
                          -k AirMOSS_retreval_5cm_col.kmz -b 2
```
