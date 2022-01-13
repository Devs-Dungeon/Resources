"""
Write a function to invert the keys and values of a dictionary.

input_dict = {'Box1':'Apple', 'Box2':'Orange'}

Expected output = {'Apple':'Box1', 'Orange':'Box2'}
"""

#Solution is:

def invert_dict(input_dict):
    output_dict = {v: k for k, v in input_dict.items()}
    return output_dict
        
        
