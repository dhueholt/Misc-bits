# tropomi_box_average
# Compute box-average for a variable. Compare average for 10 Kp=1 and 10 G2 days?

from glob import glob
# import time as t
import matplotlib.pyplot as plt
from satpy import Scene
import pdb
import numpy as np

FILENAMES = glob('/Users/dhueholt/Documents/Data/TROPOMI/20180826/PRODUCT/S5P*NO2*.nc')
print(len(FILENAMES))
SCN = Scene(reader='tropomi_l2', filenames=FILENAMES)
data_var = 'nitrogendioxide_stratospheric_column'
SCN.load([data_var])

max_lat = 67
min_lat = 45
max_lon = -75
min_lon = -125

outside_lat = np.where((SCN[data_var].latitude > max_lat) | (SCN[data_var].latitude < min_lat))
outside_lon = np.where((SCN[data_var].longitude > max_lon) | (SCN[data_var].longitude < min_lon))

mask_data = SCN[data_var].data.compute()
mask_data[outside_lat] == 0
mask_data[outside_lon] == 0

box_indices = np.nonzero(mask_data)
box_data = mask_data[box_indices]

box_average = np.nanmean(box_data)
print(box_average)
