'''
Write a Python function to convert a string date to a timestamp.

input_string = 'Jan 01 2011 08:36:40 PM'

Expected output = 1293894400.0
'''

import time
import datetime
def convert_to_ts(input_string):
    element = datetime.datetime.strptime(input_string, "%b %d %Y %I:%M:%S %p")
    timestamp = datetime.datetime.timestamp(element)
    return timestamp
