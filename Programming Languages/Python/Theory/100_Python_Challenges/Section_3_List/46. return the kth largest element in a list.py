"""
Write a function that accepts a list and the number 'k'. 
The function should return the kth largest element in the list.

Example:

input_list = [921,72,3,148,882,90,45,-1,888]

k = 2

Expected output = 888
"""

def kth_largest_element(input_list,k):
    input_list.sort()
    
    return input_list[-k]
