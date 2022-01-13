"""
Write a function to count the number of vowels in a given string.

input_string = 'dolphin'

expected output = 2
"""

def count_vowels(input_string):
    count = 0
    for i in input_string:
        if i in "aeiou":
            count += 1
        else:
            continue
    return count