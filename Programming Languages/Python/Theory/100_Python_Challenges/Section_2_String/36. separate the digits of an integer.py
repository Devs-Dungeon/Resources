"""
Write a function to separate the digits of an integer. Return the digits in the form of a list.

Example:

Input:  num = 1475

Expected output : [1,4,7,5]
"""

def separate_digits(num):
    lst = []
    for i in str(num):
        i = int(i)
        lst.append(i)
    return lst