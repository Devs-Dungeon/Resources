"""
Write a Python function that accepts three Boolean variables -  x, y, and z. 
The function should return True if at least two out of the three variables are True.

Example :

x = True, y = False, z = True

Expected output = True
"""

def booleans(x,y,z):
    if x == "True" and y == "True" and z == "False":
        result = True
        return (x, y, z, result)
    elif x == "True" and y == "False" and z == "True":
        result = True
        return (x, y, z, result)
    elif x == "False" and y == "True" and z == "True":
        result = True
        return (x, y, z, result)
    elif x == "False" and y == "False" and z == "True":
        result = False
        return (x, y, z, result)
    elif x == "False" and y == "True" and z == "False":
        result = False
        return (x, y, z, result)
    elif x == "True" and y == "False" and z == "False":
        result = False
        return (x, y, z, result)
    elif x == "True" and y == "True" and z == "True":
        result = True
        return (x, y, z, result)
    else:
        result = False
        return (x, y, z, result)
        