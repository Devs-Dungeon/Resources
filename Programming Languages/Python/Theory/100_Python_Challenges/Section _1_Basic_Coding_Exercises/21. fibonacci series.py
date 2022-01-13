"""
Write a function that randomly chooses any number 'n' from 5 to 10 (inclusive) and then generates a Fibonacci sequence until 'n'. 
The sequence should be returned in the form of a list.

Example:

for n = 5,

output_sequence = [0,1,1,2,3]
"""

import random

def Fibonacci():
    n = random.randint(5, 10)
    fibonacci_numbers = [0, 1]
    for i in range(2,n):
        fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    return n, fibonacci_numbers