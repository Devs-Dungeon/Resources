"""
Write a function that accepts a list and returns the element that has the maximum number of consecutive occurrences in the list. 
The function should also return the position at which the element was found and the count. 
If there is a tie between two positions, function should return the smallest position.

Example:

input_list = [1,13,3,3,3,4,5,6,6,3,3,3,8]

Expected output : Maximum occurring element = 3, position = 2, count = 3
"""

from itertools import groupby

def max_occur_element(input_list):
    
    temp = groupby(input_list)
    
    res = max(temp, key = lambda sub: len(list(sub[1])))
    
    max_occur_elem = res[0]
    
    init_pos = input_list.index(res[0])
    
    count = 0
    
    cur_time = 1 
    
    pre_element = None 

    for i in input_list:
        if i == pre_element:
            cur_time += 1
            count = max((cur_time, count))
        else:
            pre_element = i
            cur_time = 1
    
    return (max_occur_elem, init_pos, count)
    