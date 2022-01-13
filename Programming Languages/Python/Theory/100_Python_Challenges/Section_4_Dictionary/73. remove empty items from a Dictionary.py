"""
Write a Python function to remove empty items from the below dictionary.

input_dict = {'Box1':'Apple', 'Box2':'Mango', 'Box3': '  ', 'Box4': '  ', 'Box5':'Orange'}

Expected output : {'Box1': 'Apple', 'Box2': 'Mango', 'Box5': 'Orange'}
"""

#Solution is:

def remove_empty(input_dict):
    output_dict = {}
    
    for i, j in input_dict.items():
        if input_dict[i] != " ":
            output_dict[i] = j
            
    return output_dict
        
