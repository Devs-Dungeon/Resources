"""
Write a Python function to map two lists into a dictionary. 
list1 contains the keys, list2 contains the values.

Input lists:

list1 = [1,2,3,4,5]

list2 = [6,7,8,9,10]

Expected output:  {1: 6, 2: 7, 3: 8, 4: 9, 5: 10}
"""

#Solution is:

def map_lists(list1,list2):
    return (dict(zip(list1,list2)))
        
