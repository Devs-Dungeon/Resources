"""
Write a function that accepts a string and reverses every word of the string and then returns the reversed string. 
If the input string contains any leading or trailing spaces or multiple spaces between two words, remove the extra spaces. 
The output string should only have a single space separating the words.

Example:

input_string = ' I am   correct'

Expected output = 'correct am I'
"""

def reverse_string(input_string):
    words  = input_string.split(" ")
    reverse_words = " ".join(reversed(words))
    output_string = " ".join(reverse_words.split())
    
    return output_string