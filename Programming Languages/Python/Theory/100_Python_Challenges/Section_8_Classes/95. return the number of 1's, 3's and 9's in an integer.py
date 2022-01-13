'''
Given an integer, determine the number of 1's, 3's and 9's that fit into the number. 
Create a class and define three variables - ones, threes and nines to do this.

Example:

test1 = Ones_threes_nines(5)

Expected output:

test1.ones = 5

test1.threes = 1

test1.nines = 0

'''

class Ones_threes_nines():
    def __init__(self,num):
        self.num = num

        self.ones = self.num//1

        self.threes=self.num//3

        self.nines=self.num//9
        
test1 = Ones_threes_nines(5)