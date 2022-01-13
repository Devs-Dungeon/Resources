"""
Write a Python function that accepts a string and calculates the number of upper case letters.

sample_string = '100 Python Challenges'
expected output = 2
"""

def count_case(sample_string):
    count = 0
    for i in sample_string:
        if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
            count += 1
        else:
            pass
    return count