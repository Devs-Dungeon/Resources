"""
Write a function that accepts a number and returns True if the number is a prime number else returns False. 
A prime number is an integer which cannot be divided evenly by any integer except 1 and itself. 
You may assume that n is a non-negative integer.


"""

def prime_num(num):
    if num > 1:
        flag = False
        for i in range(2, num):
            if num % i == 0:
                flag = True
                break
    if flag:
        return False
    else:
        return True
                


        