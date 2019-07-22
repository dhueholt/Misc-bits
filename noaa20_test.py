""" Test for NOAA-20 DNB product
    Author(s): Daniel Hueholt @dhueholt GitHub
"""
from glob import glob
import matplotlib.pyplot as plt
from satpy import Scene
import cartopy.crs as ccrs
import pdb
# THIS CODE CONFIRMED TO WORK WITH NPP DATA DOWNLOADED FROM SIPS
# FILENAMES = glob('/Users/dhueholt/Documents/Data/Sips/20190306/active/*.nc')
# print(len(FILENAMES))
# SCN = Scene(reader='viirs_l1b', filenames=FILENAMES)
# SCN.load(['DNB'])
# MY_AREA = SCN['DNB'].attrs['area'].compute_optimal_bb_area({'proj': 'lcc', 'lon_0': -96.,
#                                                            'lat_0': 39., 'lat_1': 25.,
#                                                            'lat_2': 25.})
#
# NEW_SCN = SCN.resample(MY_AREA)
# NEW_SCN.save_dataset('DNB','/Users/dhueholt/Images/noaa20_test/npp_dnb_test.tif')
# CRS = NEW_SCN['DNB'].attrs['area'].to_cartopy_crs()
# lambert_proj = ccrs.LambertConformal()
# AX = plt.axes(projection=CRS)
# AX.coastlines()
# AX.gridlines()
# AX.set_global()
# plt.imshow(NEW_SCN['DNB'], transform=CRS, extent=CRS.bounds, origin='upper')
#
# CBAR = plt.colorbar()
# CBAR.set_label('DNB')
# plt.clim(0,0.0001)
# plt.savefig('/Users/dhueholt/Images/noaa20_test/npp_dnb_test_figure.png')


FILENAMES = glob('/Users/dhueholt/Documents/Data/NOAA20/20190427/active/*.nc')
print(len(FILENAMES))
SCN = Scene(reader='viirs_l1b', filenames=FILENAMES)
SCN.load(['DNB'])
MY_AREA = SCN['DNB'].attrs['area'].compute_optimal_bb_area({'proj': 'lcc', 'lon_0': -96.,
                                                           'lat_0': 39., 'lat_1': 25.,
                                                           'lat_2': 25.})

NEW_SCN = SCN.resample(MY_AREA)
NEW_SCN.save_dataset('DNB','/Users/dhueholt/Images/noaa20_test/noaa20_dnb_test.tif')
CRS = NEW_SCN['DNB'].attrs['area'].to_cartopy_crs()
lambert_proj = ccrs.LambertConformal()
AX = plt.axes(projection=CRS)
AX.coastlines()
AX.gridlines()
AX.set_global()
plt.imshow(NEW_SCN['DNB'], transform=CRS, extent=CRS.bounds, origin='upper')

CBAR = plt.colorbar()
CBAR.set_label('DNB')
plt.clim(0,0.0001)
plt.savefig('/Users/dhueholt/Images/noaa20_test/noaa20_dnb_test_figure.png')
