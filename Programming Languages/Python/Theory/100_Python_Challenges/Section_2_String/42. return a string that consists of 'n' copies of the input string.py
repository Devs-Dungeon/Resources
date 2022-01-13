"""
Write a function that accepts a string that is 'n' characters long. 
The function should return a new string that consists of 'n' copies of the input string.

Example:

input_string = 'say'

Expected output = 'saysaysay'
"""

def string_copies(input_string):
    
    output_string = input_string * len(input_string)
    
    return output_string