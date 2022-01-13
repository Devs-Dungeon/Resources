"""
Write a Python function that randomly chooses any number 'n' from 100 to 300 (inclusive) 
and then calculates the sum of the digits in the number.

Example :

n = 156

total = 12
"""

import random

def sum_digits():
    n = random.randint(100, 300)
    total = 0
    for i in str(n):
        total += int(i)
        
    return n, total
                


        