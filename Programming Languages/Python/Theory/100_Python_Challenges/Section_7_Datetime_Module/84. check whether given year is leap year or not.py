"""
Write a function to check whether a given year is leap year or not. 
If it is a leap year the function should return the string 'Leap Year' else 'Non Leap Year'.

Example:

Input: datetime.date (2020,1,1)

Expected output: 'Leap Year'
"""

def leap_year(input_date):
    if input_date.year % 4 == 0 and (input_date.year % 100 != 0 or input_date.year % 400 == 0):
        return ("Leap Year")
    else:
        return ("Non Leap Year")