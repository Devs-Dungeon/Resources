"""
Write a function that takes string characters as input and returns each characters hexadecimal value. 
The output should be in the form of a string.

input_string = 'Python'

Expected output = '50 79 74 68 6f 6e'
"""

def convert_to_hex(input_string):
    new = input_string.encode('utf-8')
    final = new.hex()
    n = 2
    return final[:n] + " " + final[n:n+2] + " " + final[n+2:n+4] + " " + final[n+4:n+6] + " " + final[n+6:n+8] + " " + final[n+8:n+10]
