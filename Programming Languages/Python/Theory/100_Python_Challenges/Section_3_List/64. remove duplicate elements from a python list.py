"""
Write a function to remove duplicate elements from a given list.

input_list = [1,2,3,4,5,6,6,5]
"""

def remove_duplicates(input_list):
    lst = []
    for i in input_list:
        if i in lst:
            pass
        else:
            lst.append(i)
    return lst
        
