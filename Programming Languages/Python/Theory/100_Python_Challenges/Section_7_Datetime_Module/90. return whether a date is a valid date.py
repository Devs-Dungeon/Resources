"""
Given the parameters day, month and year, return whether that date is a valid date.

input_date          = date (30, 2, 2021)

Expected output = False
"""

def check_date(year, month, day):
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year%4 == 0 and (year%100 != 0 or year%400 == 0):
        day_count_for_month[2] = 29
    if (1 <= month <= 12 and 1 <= day <= day_count_for_month[month]):
        return True
    else:
        return False
    