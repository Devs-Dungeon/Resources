"""
Write a function that transforms a list of characters into a list of dictionaries. 
The keys are the characters themselves and the values are the ASCII codes of those characters.

input_list = ['P', 'y', 't', 'h', 'o', 'n']

Expected output = [{'P': 80}, {'y': 121}, {'t': 116}, {'h': 104}, {'o': 111}, {'n': 110}]
"""

def to_dict(input_list):
    output_list = []
    
    for i in input_list:
        output_list.append(dict({i : ord(i)}))

    return output_list