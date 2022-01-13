"""
Write a function that finds the number of times a sub-string occurs in a given string and 
also the position (index number) at which the sub-string is found.

Example:

main_string = 'Let it be, let it be, let it be'

sub_string = 'let it be'

Expected output:

number of times sub-string occurs = 2, position =[11, 22]
"""

def find_substring(main_string, sub_string):
    value = main_string.count(sub_string)
    res = [i for i in range(len(main_string)) if main_string.startswith(sub_string, i)]
    
    return value, res