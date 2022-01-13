"""
Write a function that returns the indices of all occurrences of an element in a list. 
Return the output in the form of a list.

Example:

input_list = [10,6,7,10,9,1,-1,10]

element = 10

Expected output = [0,3,7]
"""

def indices(input_list, element):
    lst = []
    for i in range(0, len(input_list)):
        if input_list[i] == element:
            lst.append(i)
    return lst
