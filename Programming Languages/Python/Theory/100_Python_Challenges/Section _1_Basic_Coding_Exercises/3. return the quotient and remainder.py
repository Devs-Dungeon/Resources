"""
1. Write a function that accepts two integers num1 and num2. The function should divide num1 by num2
and return the quotient and remainder. The output can be rounded to 2 decimal places.
"""


def quot_rem(num1,num2):
    q = round((num1 / num2), 2)
    r = round((num1 % num2), 2)
    return (q,r)