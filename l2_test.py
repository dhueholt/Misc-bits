""" Test for VIIRS EDR product
    Author(s): Daniel Hueholt @dhueholt GitHub
"""
from glob import glob
import matplotlib.pyplot as plt
from satpy import Scene
import cartopy.crs as ccrs
import pdb

FILENAMES = glob('/Users/dhueholt/Documents/Data/Sips/CLDMSK*.nc')

SCN = Scene(reader='viirs_l2', filenames=FILENAMES)
SCN.load(['geophysical_data/Integer_Cloud_Mask'])
MY_AREA = SCN['geophysical_data/Integer_Cloud_Mask'].attrs['area'].compute_optimal_bb_area({'proj': 'lcc', 'lon_0': -96.,
                                                           'lat_0': 39., 'lat_1': 25.,
                                                           'lat_2': 25.})

NEW_SCN = SCN.resample(MY_AREA)
NEW_SCN.save_dataset('geophysical_data/Integer_Cloud_Mask','/Users/dhueholt/Documents/Hollings_2019/Images/l2/icm.tif')
CRS = NEW_SCN['geophysical_data/Integer_Cloud_Mask'].attrs['area'].to_cartopy_crs()
lambert_proj = ccrs.LambertConformal()
AX = plt.axes(projection=CRS)
AX.coastlines()
AX.gridlines()
AX.set_global()
plt.imshow(NEW_SCN['geophysical_data/Integer_Cloud_Mask'], transform=CRS, extent=CRS.bounds, origin='upper')

CBAR = plt.colorbar()
CBAR.set_label('Integer Cloud Mask')
plt.clim(-1,3)
plt.savefig('/Users/dhueholt/Documents/Hollings_2019/Images/l2/integer_cloud_mask_multiple_test.png')
