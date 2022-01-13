"""
Using sorted() function and lambda function sort the words in the list based on their second letter from a to z.

Example:

input_list =  ['coral', 'teal', 'mustard', 'blue violet', 'maroon', 'indigo', 'white', 'lime', 'navy']

Expected output = ['maroon', 'navy',  'teal',  'white',  'lime',  'blue violet',  'indigo',  'coral',  'mustard']

"""

def word_sort(input_list):
    
    k = sorted(input_list, key=lambda x:x[1])
    
    return k
