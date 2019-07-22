from glob import glob
import numpy as np
import sys

# From sips_dnb_script
start_time = '2019-04-27T01:32:00'  # ISO8601: YYYY-MM-DDTHH:mm:SS
end_time = '2019-04-27T01:12:00'




# From sips_dnb_functions
split_start = start_time.split('T')
split_end = end_time.split('T')

start_dict = {
    "year": 2019,
    "ordinal_day": 117,  # https://www.scp.byu.edu/docs/doychart.html for help
    "hour": 1,
    "minute": 11
}
end_dict = {
    "year": 2019,
    "ordinal_day": 117,
    "hour": 3,
    "minute": 18
}
data_dir = '/Users/dhueholt/Documents/Data/NOAA20/20190427'

def adjust_time(time_int):
    ''' Adjusts time to a value divisible by 6, in order to match Suomi-NPP
    and NOAA-20 data files. '''
    time_insurance = 0
    while time_int % 6 != 0:
        time_int = time_int-1
        time_insurance = time_insurance + 1
        if time_insurance > 5:
            sys.exit('Invalid time! Check inputs and try again.')

    return time_int

def time_string(time_int):
    ''' Adjusts time integer to be a string, accounting for preceding 0 '''
    if time_int < 10:
        time_str = '0' + str(time_int)
    else:
        time_str = str(time_int)

    return time_str

#
# # Test part
str_test = 'VJ102DNB'
if '02DNB' in str_test:
    print('Atomic Toaster')

# print(files_nopath)
