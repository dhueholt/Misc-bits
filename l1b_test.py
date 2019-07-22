""" Test for VIIRS NASA L1B product
    Author(s): Daniel Hueholt @dmhuehol GitHub
"""
from glob import glob
# import time as t
import matplotlib.pyplot as plt
from satpy import Scene
import cartopy.crs as ccrs
import pdb

FILENAMES = glob('/Users/dhueholt/Documents/Data/Sips/test/VNP*.nc')
SCN = Scene(reader='viirs_l1b', filenames=FILENAMES)
SCN.load(['DNB'])
MY_AREA = SCN['DNB'].attrs['area'].compute_optimal_bb_area({'proj': 'lcc', 'lon_0': -96.,
                                                               'lat_0': 39., 'lat_1': 25.,
                                                               'lat_2': 25.})
NEW_SCN = SCN.resample(MY_AREA)
NEW_SCN.save_dataset('DNB','/Users/dhueholt/Documents/Hollings_2019/Images/l1b/sips_dnb_wgs84.tif')

# lambert_proj = ccrs.LambertConformal()
# CRS = NEW_SCN['DNB'].attrs['area'].to_cartopy_crs()
# AX = plt.axes(projection=CRS)
# AX.coastlines()
# AX.gridlines()
# AX.set_global()
# plt.imshow(NEW_SCN['DNB'], transform=CRS, extent=CRS.bounds, origin='upper')
# # plt.imshow(SCN['I01'])
# CBAR = plt.colorbar()
# CBAR.set_label('DNB')
# plt.clim(0,0.00001)
# plt.savefig('/Users/dhueholt/Documents/Hollings_2019/Images/l1b/SIPS_l1b_multiple_test.png')
