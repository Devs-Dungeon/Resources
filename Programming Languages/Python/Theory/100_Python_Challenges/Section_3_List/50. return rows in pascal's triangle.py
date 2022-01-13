"""
Write a Python function that chooses a random number 'n' between 2 and 8 (inclusive) 
and returns the first n lines of the Pascal’s triangle in the form of a list.

Example:

n = 7

Expected output:

output_list = [[1],  [1, 1],  [1, 2, 1],  [1, 3, 3, 1],  [1, 4, 6, 4, 1],  [1, 5, 10, 10, 5, 1],  [1, 6, 15, 20, 15, 6, 1]]
"""

import random
def pascal_triangle():
    n = random.randint(2, 8)
    lst =[]
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        lst.append(trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]
    return n, lst
