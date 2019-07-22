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

def netcdf_units(file):
    """ Captures units of netcdf variables """
    dataset = Dataset(file)
    for var in dataset.variables:
        ncvar = dataset.variables[var]
        try:
            var_units = ncvar.units
        except AttributeError:
            var_units = 'dimensionless'
        print(var_units)
