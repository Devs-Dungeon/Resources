'''
Write a Python function to calculate the date six months from a given date using the datetime module.

input_date = date(2021, 1, 7)

Expected output = date(2021, 7, 8)
'''

import datetime
from datetime import timedelta
def add_to_date(input_date):
    output_date = input_date + timedelta(6*(365/12))
    return output_date
