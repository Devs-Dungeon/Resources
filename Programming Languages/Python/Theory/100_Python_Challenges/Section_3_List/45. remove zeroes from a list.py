"""
Write a Python function to remove zeroes from the below list.

input_list  = [1,2,0,9,7,0,2,6,0]
"""

def remove_zero(input_list):
    new_list = []
    for i in input_list:
        if i == 0:
            pass
        else:
            new_list.append(i)
    
    return new_list
