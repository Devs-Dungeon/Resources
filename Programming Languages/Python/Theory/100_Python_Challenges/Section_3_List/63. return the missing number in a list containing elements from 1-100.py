"""
Write a function that finds the missing element in a list containing elements from 1 - 100.
"""

def missing_num(input_list):
    lst = 0
    for i in range(1, 100):
        if i not in input_list:
            i = float(i)
            lst = lst + i
    return lst
            
        
