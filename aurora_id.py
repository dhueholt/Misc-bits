from glob import glob
# import time as t
import matplotlib.pyplot as plt
from satpy import Scene
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import pdb
import pyproj
import numpy as np

FILENAMES = glob('/Users/dhueholt/Documents/Data/Sips/20190427/active/VNP*.nc')
print(len(FILENAMES))
SCN = Scene(reader='viirs_l1b', filenames=FILENAMES)
SCN.load(['DNB'])
SCN.load(['dnb_lon'])
SCN.load(['dnb_lat'])

# SCN.save_dataset('DNB','/Users/dhueholt/Documents/Hollings_2019/id_testing/20190427_0830_0842_dnb.tif')

# MY_AREA = SCN['DNB'].attrs['area'].compute_optimal_bb_area({'proj': 'eqc'})
# SCN = SCN.resample(MY_AREA)

data_to_plot = SCN['DNB'].data.compute()
lats = SCN['dnb_lat'].data.compute()
min_lat = 54
aurora_thresh = 0.00003
zonal_cutoff = 5  # 3.75 km

# pdb.set_trace()
rct = 0
cct = 0
rnum = np.shape(data_to_plot)[0]
cnum = np.shape(data_to_plot)[1]
print('Starting loop!')
while rct < rnum:
    for cct in range(1,cnum):
        if lats[rct,cct] < min_lat:  # If we've checked all the high latitudes already
            break
        if data_to_plot[rct,cct] > aurora_thresh:
            pdb.set_trace()
            rctg = rct
            while cct < cnum:
                print(data_to_plot[rct,cct])
                if data_to_plot[rct,cct] > aurora_thresh:
                    rctg[cct] = cct  # Add this index to the list
                else:  # Eventually, a pixel will be less than the threshold
                    if len(rctg) > zonal_cutoff:  # If we've counted enough bright pixels
                        data_to_plot[rct,rctg] = 0  # Null them all
                        break  # Continue the parent while loop
                    else:  # If there aren't enough bright pixels
                        break  # Move on
                cct = cct+1
    rct = rct+1



data_to_plot[greater_than] = 0

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
data_plot = plt.pcolormesh(SCN['dnb_lon'].data, SCN['dnb_lat'].data, data_to_plot, transform=PlateCarree)
CBAR = plt.colorbar(data_plot, ax=AX)
CBAR.set_label('DNB')
AX.set_xlim(-125,-75)
AX.set_ylim(45,67)
AX.add_feature(cfeat.STATES, edgecolor='black')
plt.clim(0, 0.0001)
#plt.show()
plt.savefig('/Users/dhueholt/Documents/Hollings_2019/id_testing/20190427_0830_0842_DNB_aurthresh3e-5.png')
