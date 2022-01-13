"""
Write a function that accepts two arguments year and month, and then checks if the month has Friday the 13th.

Example:

year = 2020, month = 3

Expected output = True
"""


from datetime import datetime
 
def check_friday_13(yr, mon):
    user_date = datetime(yr, mon, 13)
    if user_date.strftime("%A") == "Friday":
        return datetime(yr, mon, 13), True
    else:
        return datetime(yr, mon, 13), False