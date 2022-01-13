"""
Write a Python function that chooses random values for the year, month and day within the specified valid ranges 
and then subtract five days from this date.

Example:

chosen_date =  datetime.date(3683, 12, 16)

Expected output = datetime.date(3683, 12, 11)
"""

import datetime
import random
def subtract_days():
    start_date = datetime.date(2020, 1, 1)
    
    end_date = datetime.date(2030, 1, 1)

    time_between_dates = end_date - start_date
    
    days_between_dates = time_between_dates.days
    
    random_number_of_days = random.randrange(days_between_dates)
    
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    
    next_day = random_date - datetime.timedelta(days=5)
    
    return (random_date, next_day)
    