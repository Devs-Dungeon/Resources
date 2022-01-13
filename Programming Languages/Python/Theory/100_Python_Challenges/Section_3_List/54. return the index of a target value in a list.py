"""
Write a function that accepts a sorted list and a target value. 
If the target value is found in the list, the function should return the index of the target value. 
If not, return the index where it would be if it were inserted in order.

Example:

input_list = [0,1,5,7,8]

target value = 6

Expected output : index = 3
"""

def return_index(input_list, target):
    if target in input_list:
        return input_list.index(target)
    else:
        input_list.append(target)
        input_list.sort()
        return input_list.index(target))
