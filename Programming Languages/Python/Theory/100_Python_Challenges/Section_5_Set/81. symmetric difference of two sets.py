"""
Write a function to find the elements which are in either of the sets, but not in their intersection.

set1 = {1,2,3,4,5}

set2 = {4,5,6,7,8}
"""

def sym_diff(set1,set2):
    return set1.symmetric_difference(set2)
    