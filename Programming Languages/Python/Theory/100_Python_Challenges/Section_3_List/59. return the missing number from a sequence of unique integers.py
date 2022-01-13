"""
Write a function that accepts a list containing n distinct elements in the range 0 to n 
and returns the only number in the range that is missing from the list.

Example:

input_list = [0,3,2,1,5]

Expected output = 4
"""

def missing_number(input_list):
    n = max(input_list)
    for i in range(0, n):
        if i in input_list:
            pass
        else:
            return i
