"""
Write a function that combines two lists by alternatingly taking elements from both the lists.

input_list1 = ['a', 'b', 'c']

input_list2 = ['x', 'y', 'z']

Expected output = ['a', 'x', 'b', 'y', 'c', 'z']
"""

def concat_list(input_list1, input_list2):
    result = [None]*(len(input_list1)+len(input_list2))
    result[::2] = input_list1
    result[1::2] = input_list2
    return result