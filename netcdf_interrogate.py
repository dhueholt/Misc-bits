""" Interrogate netCDF variables and attributes
    Author(s): Daniel Hueholt @dmhuehol GitHub
"""

from netCDF4 import Dataset
def netcdf_printer(file):
    """Prints basic netCDF file features to command window"""
    dataset = Dataset(file)
    print(dataset)
    print(dataset.file_format)
    for attr in dataset.ncattrs():
        print(attr, '=', getattr(dataset, attr))
    for var in dataset.variables:
        print(var)
