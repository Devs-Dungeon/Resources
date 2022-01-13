"""
1. Write a function that accepts three variables a,b,c and returns the sum of these variables, if the 
values are equal then return two times their sum.
"""


def sum_num(a,b,c):
    if a == b == c:
        return 2 * (a+b+c)
    else:
        return (a+b+c)