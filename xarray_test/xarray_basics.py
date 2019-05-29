import numpy as np
import pandas as pd
import xarray as xr
import time as t

## Make xarray without specifying coordinates or dimensions
#randx = xr.DataArray(np.random.randn(2,3))
#print(randx)

## Make xarray with coordinates and dimensions
#data = xr.DataArray(np.random.randn(2,3), coords={'x':['a','b']},dims=('x','y'))
#print(data)

## Make xarray from pandas object
#panda_test = xr.DataArray(pd.Series(range(2),index=list('ab'),name='ph'))
#print(panda_test)

## The Four Ways to Index
# random_data = xr.DataArray(np.random.randn(2,3), coords={'x':['a','b']},dims=('x','y'))
# print(random_data)
# print()
# #t.sleep(3)
#
# print('Indexed by positional and integer label, NumPy style [[0,1]]')
# index_positionAndLabel = random_data[[0,1]]
# print(index_positionAndLabel)
# #t.sleep(3)
#
# print('Indexed by positional and coordinate label, pandas style')
# index_positionAndCoordinate = random_data.loc['a':'b']
# print(index_positionAndCoordinate)
#
# print('Indexed by dimension name and integer label, xarray style')
# index_dimnameAndLabel = random_data.isel(x=slice(2)) # .isel is an xarray function to extract entries by integer
# #slice syntax is slice(stop) or slice(start,step,stop)
# print(index_dimnameAndLabel)
#
# print('Indexed by dimension name and coordinate label, xarray style')
# index_dimnameAndCoordinate = random_data.sel(x=['a','b']) # .sel is an xarray function to extract entries by coordinate labels
# print(index_dimnameAndCoordinate)

## NumPy/xarray interactions
# NumPy operations work on xarrays
more_random_data = xr.DataArray(np.random.randn(2,3), coords={'panda_horse':['a','b']},dims=('panda_horse','pmt'))
# print(more_random_data)
# more_random_data_plus = more_random_data+10
# print(more_random_data_plus)
# more_random_data_sin = np.sin(more_random_data)
# And they let you designate dimension names instead of just axis numbers!
a_random_mean = more_random_data.mean(dim='pmt')
print(a_random_mean)
