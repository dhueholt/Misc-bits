""" TROPOMI product in aurora box of interest
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

FILENAMES = glob('/Users/dhueholt/Documents/Data/TROPOMI/20181214/S5P*NO2*.nc')
print(len(FILENAMES))
SCN = Scene(reader='tropomi_l2', filenames=FILENAMES)
# pdb.set_trace()
SCN.load(['nitrogendioxide_stratospheric_column'])
lambert_proj = ccrs.LambertConformal()
PlateCarree = ccrs.PlateCarree()
fig = plt.figure(frameon=False)
fig.set_size_inches(16,10)
AX = plt.axes(projection=PlateCarree)
AX.coastlines()
AX.gridlines()
AX.set_global()

# pdb.set_trace()
data_plot = plt.pcolormesh(SCN['nitrogendioxide_stratospheric_column'].longitude, SCN['nitrogendioxide_stratospheric_column'].latitude, SCN['nitrogendioxide_stratospheric_column'].data, transform=PlateCarree)
cbar = plt.colorbar(data_plot, ax=AX)
cbar.set_label('NO2 stratospheric column')
AX.set_xlim(-125,-75)
AX.set_ylim(45,67)
AX.add_feature(cfeat.STATES, edgecolor='black')
plt.clim(0,0.0001)
plt.savefig('/Users/dhueholt/Documents/Hollings_2019/aurora_images/20181214_1728_2051_NO2strat.png')
