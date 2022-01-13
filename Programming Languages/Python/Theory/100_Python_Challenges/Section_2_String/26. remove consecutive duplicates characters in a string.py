"""
Write a function that accepts a string as an argument and 
modifies the string so as to remove all consecutive duplicate characters.

Example:

input_string =  'mississauga'

Expected output = 'misisauga'
"""

def remove_duplicates(input_string):
    output_string = ''
    
    for chr in input_string:
        if output_string == '' or chr != output_string[len(output_string)-1]:
            output_string += chr
            
    return output_string
