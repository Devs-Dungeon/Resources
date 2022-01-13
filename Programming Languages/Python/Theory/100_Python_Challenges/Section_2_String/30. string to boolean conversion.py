"""
Write  a function that converts a string to Boolean value. 
If the input string contains the value “true” (if required convert the case) then the Boolean value after conversion should be - True. 
If the input string contains the value “false” then the Boolean value after  conversion should be - False.  
If the string contains any other value other than “true” or "false" then the converted value should be “Invalid input”.

Example:

input_string = 'TRUE'

Expected output = True
"""

def string_to_bool(input_string):
    input_string = input_string.upper()
    if input_string == "TRUE":
        return True
    elif input_string == "FALSE":
        return False
    else:
        return "Invalid input"
    
