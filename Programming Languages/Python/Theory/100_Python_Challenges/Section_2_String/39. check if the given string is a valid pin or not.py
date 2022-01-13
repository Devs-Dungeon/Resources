"""
Write a function that tests if a string is a valid pin or not.

A valid pin has:

1. Exactly 5 characters.

2. Accepts only numerical characters (0-9).

3. No whitespaces.

Example:

input_string = "89abc"

Expected output = False


"""

def valid_pin(input_string):
    if len(input_string) != 5:
        return False
        
    if not input_string.isdigit():
        return False
        
    if " " in input_string:
        return False
        
    else:
        return True