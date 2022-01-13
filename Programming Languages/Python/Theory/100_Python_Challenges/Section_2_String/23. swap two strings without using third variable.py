"""
Write a function that swaps two strings without using a third variable.

Example:

s1 = 'abcdef'

s2 = '123456'

Expected output :

s1 = '123456'

s2 = 'abcdef'
"""

def swap_strings(s1,s2):
    s1, s2 = s2, s1
    return s1, s2