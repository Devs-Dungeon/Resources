"""
Write a Python function to sum all the values in a dictionary and return the total value.

input_dict = {'a':100,'b':-54,'c':247}
"""

#Solution is:

def sum_values(input_dict):
    total = 0
    for i in input_dict.values():
        total += i
    return total

        
        
