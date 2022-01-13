"""
Write a Python function to multiply all the values in a dictionary.

input_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

#Solution is:

def multiply_values(input_dict):
    product = 1
    for i in input_dict.values():
        product *= i
    return product

        
        
