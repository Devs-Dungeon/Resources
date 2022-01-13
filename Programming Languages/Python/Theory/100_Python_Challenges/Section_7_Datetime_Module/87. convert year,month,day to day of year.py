"""
Write a Python function that chooses random values for the year, month and day within the specified valid ranges 
and then your function should convert Year/Month/Day of the chosen date to Day of Year.

Example:

chosen_date = datetime.date(8004, 4, 23)

day_of_the_year = 114
"""

import random
import datetime
def day_of_year():
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2030, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    
    day_of_the_year = random_date.strftime('%j')
    return (random_date, day_of_the_year)
    