from satpy import Scene
from glob import glob
import matplotlib.pyplot as plt
import time as t

filenames = glob('/Users/dhueholt/Documents/Data/test/*20190201*.h5')
# print(filenames)
# t.sleep(2)
# print("Continuing")

scn = Scene(reader='viirs_sdr', filenames=filenames)
scn.load(['I04'])
my_area = scn['I04'].attrs['area'].compute_optimal_bb_area({'proj': 'lcc', 'lon_0': -95., 'lat_0': 25., 'lat_1': 25., 'lat_2': 25.})
new_scn = scn.resample(my_area)

crs = new_scn['I04'].attrs['area'].to_cartopy_crs()
ax = plt.axes(projection=crs)

ax.coastlines()
ax.gridlines()
ax.set_global()
plt.imshow(new_scn['I04'], transform=crs, extent=crs.bounds, origin='upper')
cbar = plt.colorbar()
cbar.set_label("Kelvin")
#plt.show()
plt.savefig('/Users/dhueholt/Documents/Hollings_2019/I04_test.png')
