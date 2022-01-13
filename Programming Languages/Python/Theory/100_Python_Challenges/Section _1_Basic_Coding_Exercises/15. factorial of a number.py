"""
Write a Python function that randomly chooses any number from 1 to 10 (inclusive) 
and then calculates the factorial of the number.

Example :

num = 5

factorial = 5*4*3*2*1 = 120
"""

import random

def factorial():
    k = random.randint(1,10)
    num = 1
    for i in range(1, k+1):
        num *= i
    return (k, num)

        