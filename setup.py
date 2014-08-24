#!/usr/bin/env python

from distutils.core import setup
import glob

scriptsList = glob.glob('*.py')

setup(name='AirMOSS_GDAL_Utils',
      description = 'Utility scipts for working with AirMOSS data and retrevals using GDAL',
      author = 'Daniel Clewley',
      author_email = 'daniel.clewley@gmail.com',
      url = 'http://mixil.usc.edu/',
      scripts=scriptsList)
