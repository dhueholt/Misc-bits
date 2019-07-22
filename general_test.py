""" Test for VIIRS EDR product
    Author(s): Daniel Hueholt @dhueholt GitHub
"""
from glob import glob
import matplotlib.pyplot as plt
from satpy import Scene
import cartopy.crs as ccrs
import pdb

FILENAMES = glob('/Users/dhueholt/Documents/Data/CloudMask/20190306/JRR*.nc')

SCN = Scene(reader='viirs_edr_gran', filenames=FILENAMES)
SCN.load(['cloudmaskbinary'])
MY_AREA = SCN['cloudmaskbinary'].attrs['area'].compute_optimal_bb_area({'proj': 'lcc', 'lon_0': -96.,
                                                           'lat_0': 39., 'lat_1': 25.,
                                                           'lat_2': 25.})

NEW_SCN = SCN.resample(MY_AREA)
# pdb.set_trace()
NEW_SCN.save_dataset('cloudmaskbinary','/Users/dhueholt/Images/cmb.png')
CRS = NEW_SCN['cloudmaskbinary'].attrs['area'].to_cartopy_crs()
lambert_proj = ccrs.LambertConformal()
AX = plt.axes(projection=CRS)
AX.coastlines()
AX.gridlines()
AX.set_global()
plt.imshow(NEW_SCN['cloudmaskbinary'], transform=CRS, extent=CRS.bounds, origin='upper')

# CBAR = plt.colorbar()
# CBAR.set_label('cloudmaskbinary')
# plt.clim(-4,4)
plt.savefig('/Users/dhueholt/Images/reference_1.png')
