"""
Write a Python function to remove duplicates from Dictionary.

Input data:

input_dict =  {'Box1':'Apple', 'Box2':'Mango', 'Box3':'Orange', 'Box4':'Apple', 'Box5':'Orange', 'Box6':'Orange','Box7':'Strawberry','Box8':'Apple'}

Expected output = {'Box2': 'Mango', 'Box6': 'Orange', 'Box7': 'Strawberry', 'Box8': 'Apple'}
"""

#Solution is :

def remove_duplicates(input_dict):
    output_dict = {}
    for key,value in input_dict.items():
        if value not in output_dict.values():
            output_dict[key] = value
    return output_dict
        
