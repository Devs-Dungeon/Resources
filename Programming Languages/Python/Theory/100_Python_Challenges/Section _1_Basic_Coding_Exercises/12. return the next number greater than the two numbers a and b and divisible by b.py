"""
Given two numbers a and b. 
Create a function that returns the next number greater than a and b and divisible by b. (a>b)

Example:

a = 25, b = 5

Expected output = 30
"""

def check_division(a,b):
    if a > b:
        for num in range(1, a+b+1):
            if num % b == 0 and num > a and num > b:
                return num
            else:
                continue