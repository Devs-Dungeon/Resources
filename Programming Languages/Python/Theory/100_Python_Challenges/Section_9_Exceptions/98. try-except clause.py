"""
Write a function that accepts 2 parameters 'a' and 'b' . 
Your function should execute the equation 'a/b' and if this equation raises any exception, the exception should be returned else return the quotient.

Template:

def validate(a,b):
    try:
         a/b
    except ValueError:
         return (ValueError)
 
    except _ _ _ _ _ _:
           _ _ _ _ _ _ 

"""

#Solution is:

def validate(a,b):
    try:
        return a/b
        
    except TypeError:
        return TypeError
        
    except ZeroDivisionError:
        return ZeroDivisionError
    
    else:
        return a//b
        
