"""
Write a function that concatenates n input lists, where n is variable.

Example:

          n             = [1,2,3],[4,5,6],[7,8],[9]

Expected output =  [1,2,3,4,5,6,7,8,9]
"""

import itertools

def concat(*n):
    
    lst = list(itertools.chain(*n))
    
    return lst
