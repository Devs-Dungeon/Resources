"""
Write a function to remove all occurrences of the number '20' from the below list.

input_list = [5, 20, 15, 20, 25, 50, 20]
"""

def remove_20(input_list):
    
    lst = [i for i in input_list if i != 20]
    
    return lst
