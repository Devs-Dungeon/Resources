"""
Write a function that returns the previous day and the next day of a given date. 
The output should be in the following format - (prev_day,input_date,next_day).

input_date = date(2020,12,31)
"""

import datetime
def calculate_dates(input_date):
    prev_day = input_date - datetime.timedelta(days=1)
    next_day = input_date + datetime.timedelta(days=1)
    return (prev_day, input_date, next_day)