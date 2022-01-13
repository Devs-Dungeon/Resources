"""
Write a Python function that generates a list named 'input_list' containing 10 random numbers ranging from 0-100, 
and then the function should return a list of numbers divisible by fifteen from the 'input_list'.

Example:

input_list = [15,30,45,46,47,60,75,99,100]

output_list = [15, 30, 45, 60, 75]
"""

import random

def divide_by_15():
    input_list = []
    output_list = []
    for i in range(1, 11):
        k = random.randint(0, 100)
        input_list.append(k)
        
    for item in input_list:
        if item % 15 == 0:
            output_list.append(item)
            
    return input_list, output_list
                


        