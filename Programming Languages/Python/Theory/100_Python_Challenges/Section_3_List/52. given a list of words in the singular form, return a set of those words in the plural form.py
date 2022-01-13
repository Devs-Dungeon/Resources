"""
Given a list of words in the singular form, 
return a set of those words in the plural form if they appear more than once in the list.



Example:

input_list = ["table", "chair", "chair", "chair","desk","desk"]

Expected output = ['table', 'desks', 'chairs']
"""

def pluralize(input_list):
    lst = []
    new = []
    for i in input_list:
        if input_list.count(i) > 1:
            lst.append(i + "s")
        else:
            lst.append(i)
            
    for j in lst:
        if j in new:
            pass
        else:
            new.append(j)
            
    k = set(new)
    l = list(k)
    return l
