# Scratch work for figuring out how to mimic variable style for unit tests

import numpy as np
from xarray import DataArray

DEFAULT_FILE_DTYPE = np.float32
DEFAULT_FILE_SHAPE = (768, 3200)
DEFAULT_FILE_DATA = np.arange(DEFAULT_FILE_SHAPE[0] * DEFAULT_FILE_SHAPE[1],
                              dtype=DEFAULT_FILE_DTYPE).reshape(DEFAULT_FILE_SHAPE)
DEFAULT_FILE_FACTORS = np.array([2.0, 1.0], dtype=np.float32)
DEFAULT_LAT_DATA = np.linspace(58, 71, DEFAULT_FILE_SHAPE[1]).astype(DEFAULT_FILE_DTYPE)
DEFAULT_LAT_DATA = np.repeat([DEFAULT_LAT_DATA], DEFAULT_FILE_SHAPE[0], axis=0)
DEFAULT_LON_DATA = np.linspace(-93, -22, DEFAULT_FILE_SHAPE[1]).astype(DEFAULT_FILE_DTYPE)
DEFAULT_LON_DATA = np.repeat([DEFAULT_LON_DATA], DEFAULT_FILE_SHAPE[0], axis=0)

file_content = {
        'satellite_name': 'NPP',
        'instrument_name': 'VIIRS',
        'title': 'JRR-CloudMask',
        'start_orbit_number': 38106,
        'end_orbit_number': 38106,
        # '/attr/time_coverage_start': dt.strftime('%Y-%m-%dT%H:%M:%SZ'),
        # '/attr/time_coverage_end': (dt + timedelta(minutes=6)).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'resolution': '750M'
    }
file_content['Latitude'] = DataArray(DEFAULT_LAT_DATA, dims=('Rows','Columns'))
file_content['Latitude'].attrs['units'] = 'degrees_north'
file_content['Latitude'].attrs['_FillValue'] = -999.9

print(file_content.satellite_name)
