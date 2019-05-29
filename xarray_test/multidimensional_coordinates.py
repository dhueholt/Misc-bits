import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np

ds = xr.tutorial.open_dataset('rasm').load()

print(ds.xc.attrs)
print(ds.yc.attrs)

#fig,(ax1,ax2) = plt.subplots(ncols=2, figsize=(9,3))
#ds.xc.plot(ax=ax1)
#ds.yc.plot(ax=ax2)
#plt.savefig('/Users/dhueholt/Documents/Hollings_2019/xarray_test/test_plot.png') #Plots a scalar field xc,yc

#Tair_test = ds.Tair[0].plot()
#plt.savefig('/Users/dhueholt/Documents/Hollings_2019/xarray_test/Tair_test.png') #Plots onto logical coordinates

# plt.figure(figsize=(7,2))
# ax = plt.axes(projection=ccrs.PlateCarree())
# ds.Tair[0].plot.pcolormesh(ax=ax,transform=ccrs.PlateCarree(),x='xc',y='yc',add_colorbar=True)
# ax.coastlines()
# plt.savefig('/Users/dhueholt/Documents/Hollings_2019/xarray_test/Tair_true.png')
#
# lat_bins = np.arange(0,91,2)
# lat_center = np.arange(1,90,2)
# Tair_lat_mean = (ds.Tair.groupby_bins('xc',lat_bins,labels=lat_center).mean(xr.ALL_DIMS))
# #print(Tair_lat_mean) #Shows that xc coordinate is now xc_bins coordinate
# Tair_lat_mean.plot()
# plt.savefig('/Users/dhueholt/Documents/Hollings_2019/xarray_test/Tair_by_latitude.png')
