"""
Write a Python function that takes a division equation d and checks 
if it returns a whole number without decimals after dividing.

Examples:

check_division(4/2) ➞ True

check_division(25/2) ➞ False
"""

def check_division(num):
    if num % 2 == 0:
        return num, True
    else:
        return num, False

        