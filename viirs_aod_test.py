""" Test for VIIRS EDR product
    Author(s): Daniel Hueholt @dmhuehol GitHub
"""
from glob import glob
# import time as t
import matplotlib.pyplot as plt
from satpy import Scene

FILENAMES = glob('/Users/dhueholt/Documents/Data/AOD/*AOD*.nc')
# print(filenames)
# t.sleep(2)
# print("Continuing")

SCN = Scene(reader='viirs_gran', filenames=FILENAMES)
SCN.load(['aod550'])
MY_AREA = SCN['aod550'].attrs['area'].compute_optimal_bb_area({'proj': 'lcc', 'lon_0': -95.,
                                                               'lat_0': 25., 'lat_1': 25.,
                                                               'lat_2': 25.})
NEW_SCN = SCN.resample(MY_AREA)

CRS = NEW_SCN['aod550'].attrs['area'].to_cartopy_crs()
AX = plt.axes(projection=CRS)

AX.coastlines()
AX.gridlines()
AX.set_global()
plt.imshow(NEW_SCN['aod550'], transform=CRS, extent=CRS.bounds, origin='upper')
CBAR = plt.colorbar()
CBAR.set_label("aod550")
#plt.show()
plt.savefig('/Users/dhueholt/Documents/Hollings_2019/AOD_test.png')
