"""
Write a function to multiply all elements in a given list and return the product.

input_list = [1,2,3,4,5,6,6,5]
"""

def multiple_elements(input_list):
    product = 1
    for i in input_list:
        product = product * i
    return product
    
