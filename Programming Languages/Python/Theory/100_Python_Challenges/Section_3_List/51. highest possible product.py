"""
Write a function that returns the highest possible product by multiplying 3 numbers from the given list.

input_list = [20,7,3,6,-1,0,9]
"""

def highest_prod(input_list):
    input_list.sort()
    lst = input_list
    prod = lst[-1] * lst[-2] * lst[-3]
    
    return prod
