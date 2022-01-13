"""
Write a function that accepts two arguments - start_of_range and end_of_range , 
and returns a list containing all the numbers inclusive to that range.

Examples:

inclusive_list(1, 5) - [1,2,3,4,5]

inclusive_list(10,5) - [10,9,8,7,6,5]
"""

def inclusive_list(start, end):
    lst1 = []
    lst2 = []
    if start < end:
        for i in range(start, end+1):
            lst1.append(i)
        return lst1
    else:
        for i in range(end, start+1):
            lst2.append(i)
        lst2 = lst2[::-1]
        return lst2
            
        
