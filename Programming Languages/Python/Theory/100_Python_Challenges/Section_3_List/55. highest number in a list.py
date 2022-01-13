"""
Write a Python function that returns the highest number in a list.

input_list = [9,6,45,67,12]

Expected output =  67
"""

def high_num(input_list):
    
    input_list.sort()
    
    return input_list[-1]
    
