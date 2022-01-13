'''
Create methods for the Calculator class that can do the following:

Add two numbers

Subtract two numbers

Multiply two numbers

Divide two numbers

The methods accept the parameters x and y. The output can be rounded to 2 decimal places.

'''

class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def add(self):
        value_add = self.x + self.y
        return self.x,self.y,value_add
        
    def sub(self):
        value_sub = self.x - self.y
        return self.x,self.y,value_sub
        
    def mul(self):
        value_mul = self.x * self.y
        return self.x,self.y,value_mul
        
    def div(self):
        value_div = self.x / self.y
        return (self.x,self.y,value_div)