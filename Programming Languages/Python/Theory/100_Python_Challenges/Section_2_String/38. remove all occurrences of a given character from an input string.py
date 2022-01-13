"""
Write a function that accepts a string and a character. 
The function should remove all occurrences of the given character from the input string and return the string.

Example:

input_string = 'technique'

char = 'e'

Expected output = 'tchniqu'
"""

def remove_char(input_string, char):
    new_str = ""
    for i in input_string:
        if i == char:
            pass
        else:
            new_str = new_str + i
            
    return new_str