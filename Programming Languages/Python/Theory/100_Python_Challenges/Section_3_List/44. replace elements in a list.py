"""
Write a function that finds the value 'd' in the given list and then replaces the string 'd' with the string 'c'.

input_list = ['a', 'b', 'd', 'd', 'e', 'd', 'g']

expected output = ['a', 'b', 'c', 'c', 'e', 'c', 'g']
"""

def replace_value(input_list):
    
    modified_list = ["c" if x == "d" else x for x in input_list]
    
    return modified_list
