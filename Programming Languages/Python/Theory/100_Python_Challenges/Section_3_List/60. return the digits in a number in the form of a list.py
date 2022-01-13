"""
Write a function that accepts a number and returns its digits in a list.

Example:

num = 1234

Expected output = [1,2,3,4]
"""

def num_to_list(num):
    lst = []
    for i in str(num):
        i = int(i)
        lst.append(i)
    return lst
        
