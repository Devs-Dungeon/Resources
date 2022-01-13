"""
Write a Python function to get a string made of the first 2 and the last 2 chars from a given input string. 
If the length of input string is less than 2, return an empty string - ''.

Example:

input_string = 'Python'

Expected output  = 'Pyon'
"""

def str_first2_last2_char(input_string):
    
    if len(input_string) < 2:
        return ""
    else:
        output_string = input_string[0:2] + input_string[-2:]
        return output_string
    
    