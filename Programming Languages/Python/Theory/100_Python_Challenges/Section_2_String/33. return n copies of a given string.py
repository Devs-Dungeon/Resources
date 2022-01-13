"""
Write a function that returns a string which is 'n' copies of a given string.

Example:

input_string = 'xyz'

n = 3

Expected output: 'xyzxyzxyz'
"""

def copies_of_string(input_string,num):
    output_string = input_string * num
    return output_string