"""
Write a function that chooses a random number 'n' from 1 and 5000 (inclusive) and then calculates the length of this number 'n'. 
Do not use the built-in function 'len' to calculate the length.

Example:

n =1000

length = 4
"""

import random

def calculate_length():
    n = random.randint(1,5000)
    count = 0
    for i in str(n):
        count += 1
    
    return (n, count)