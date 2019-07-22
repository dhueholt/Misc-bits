""" Test for TROPOMI product
    Author(s): Daniel Hueholt @dmhuehol GitHub
"""
from glob import glob
# import time as t
import matplotlib.pyplot as plt
from satpy import Scene
import cartopy.crs as ccrs
import pdb

FILENAMES = glob('/Users/dhueholt/Documents/Data/TROPOMI/20180826/PRODUCT/S5P*CO*.nc')
# print(filenames)
# t.sleep(2)
# print("Continuing")

SCN = Scene(reader='tropomi_l2', filenames=FILENAMES)

pdb.set_trace()
SCN.load(['nitrogendioxide_tropospheric_column'])
MY_AREA = SCN['nitrogendioxide_tropospheric_column'].attrs['area'].compute_optimal_bb_area({'proj': 'lcc', 'lon_0': -96.,
                                                                                           'lat_0': 39., 'lat_1': 25.,
                                                                                           'lat_2': 25.})
# import pdb; pdb.set_trace()
NEW_SCN = SCN.resample(MY_AREA)

CRS = NEW_SCN['nitrogendioxide_tropospheric_column'].attrs['area'].to_cartopy_crs()
lambert_proj = ccrs.LambertConformal()
AX = plt.axes(projection=CRS)

AX.coastlines()
AX.gridlines()
AX.set_global()
plt.imshow(NEW_SCN['nitrogendioxide_tropospheric_column'], transform=CRS, extent=CRS.bounds, origin='upper')
# plt.imshow(SCN['nitrogendioxide_tropospheric_column'])
CBAR = plt.colorbar()
CBAR.set_label('nitrogendioxide_tropospheric_column')
plt.clim(0, 0.0001)
#plt.show()
plt.savefig('/Users/dhueholt/Documents/Hollings_2019/tropomi_global_test.png')
