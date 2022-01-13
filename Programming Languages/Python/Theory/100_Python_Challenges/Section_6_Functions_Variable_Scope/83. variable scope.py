"""
The following code should return the sum of 3 variables a, b, c. 
If you execute the code below, Python throws an 'UnboundLocalError' exception, meaning we are trying to access a variable that is not in scope. 
Correct the code below and return the sum of a, b, c.

def scope():
    a = 5
    def outer():
        b = 10
        return (res1+b)
        def inner():
            c = 15
            return (c)
        res1 = inner()
    res2 = outer()    
    return (res2+a)

"""

#Solution is:

def scope():
    a = 5
    def outer():
        b = 10
        return (res1+b)
        
    def inner():
        c = 15
        return (c)
        
    res1 = inner()
    res2 = outer()    
    
    return (res2+a)
