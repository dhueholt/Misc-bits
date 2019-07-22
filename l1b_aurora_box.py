""" VIIRS DNB product in aurora box of interest
    Author(s): Daniel Hueholt @dmhuehol GitHub
"""
from glob import glob
# import time as t
import matplotlib.pyplot as plt
from satpy import Scene
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import pdb
import pyproj

FILENAMES = glob('/Users/dhueholt/Documents/Data/Sips/20181214/VNP*.nc')
print(len(FILENAMES))
SCN = Scene(reader='viirs_l1b', filenames=FILENAMES)
SCN.load(['DNB'])
SCN.load(['dnb_lon'])
SCN.load(['dnb_lat'])
# MY_AREA = SCN['DNB'].attrs['area'].compute_optimal_bb_area({'proj': 'lcc', 'lon_0': -96.,
                                                               # 'lat_0': 39., 'lat_1': 25.,
                                                               # 'lat_2': 25.})
# NEW_SCN = SCN.resample(MY_AREA)
SCN.save_dataset('DNB','/Users/dhueholt/Documents/Hollings_2019/aurora_images/20181214_06480718_08360906_dnb.tif')

# CRS = NEW_SCN['DNB'].attrs['area'].to_cartopy_crs()
# lambert_proj = ccrs.LambertConformal()
PlateCarree = ccrs.PlateCarree()
fig = plt.figure(frameon=False)
fig.set_size_inches(16,10)
AX = plt.axes(projection=PlateCarree)
AX.coastlines()
AX.gridlines()
AX.set_global()
# pdb.set_trace()
data_plot = plt.pcolormesh(SCN['dnb_lon'].data, SCN['dnb_lat'].data, SCN['DNB'].data, transform=PlateCarree)

# plt.imshow(NEW_SCN['DNB'], transform=CRS, extent=CRS.bounds, origin='upper')
#
# isn2004=pyproj.Proj("+proj=lcc +lat_1=25 +lat_2=25 +lat_0=39 +lon_0=-96")
# wgs84=pyproj.Proj("+init=EPSG:4326") # LatLon with WGS84 datum used by GPS units and Google Earth
# left, bottom = isn2004(-125, 42)  # longitude E, latitude N
# right, top = isn2004(-75, 67)  # longitude E, latitude N
# AX.set_xlim(left,right)
# AX.set_ylim(bottom, top)

CBAR = plt.colorbar(data_plot, ax=AX)
CBAR.set_label('DNB')
AX.set_xlim(-125,-75)
AX.set_ylim(45,67)
AX.add_feature(cfeat.STATES, edgecolor='black')
plt.clim(0, 0.0001)
#plt.show()
plt.savefig('/Users/dhueholt/Documents/Hollings_2019/aurora_images/20181214_06480718_08360906_DNB.png')
