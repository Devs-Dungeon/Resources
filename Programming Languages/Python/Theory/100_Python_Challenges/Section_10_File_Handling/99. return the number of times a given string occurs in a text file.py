"""
Write a function that accepts a string as an input and checks if the input string is present in a text file. 
The function should return the number of times the string occurs in the text file.

Example:

Input filename = input.txt

word : 'it'

Expected output = 1
"""

def read_text_file(word):
    with open("input.txt") as f:
        content = f.read()
        value = content.count(word)
        
    return value

