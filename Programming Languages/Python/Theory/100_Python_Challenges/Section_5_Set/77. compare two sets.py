"""
Write a Python function to display a set containing all the numbers from set1 which are not present in set2.

set1 = set([2,4,6,8,9,10])

set2 = set([1,3,5,7,9,11])
"""

def compare_sets(set1, set2):
    set1.difference_update(set2)
    return set1