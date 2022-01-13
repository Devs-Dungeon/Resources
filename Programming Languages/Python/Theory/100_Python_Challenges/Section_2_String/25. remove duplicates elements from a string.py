"""
Write a function to remove duplicate elements from a Python string.

input_string  = 'How are you?'

Expected output = How areyu?
"""

def remove_duplicates(input_string):
    new = ""
    for i in input_string:
        if(i in new):
            pass
        else:
            new = new + i
    
    return new