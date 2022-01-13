"""

Write a function that calculates the number of numerical digits in a string.

Example:

input_string = 'gkoi6544'

Expected output = 4

"""


def count_num_digits(input_string):
    count = 0
    for i in input_string:
        if i.isdigit():
            count +=1
        else:
            continue
    
    return count