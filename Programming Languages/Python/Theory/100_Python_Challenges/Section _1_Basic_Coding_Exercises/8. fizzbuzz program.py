"""

Write a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz". 
If the number is a multiple of 3, the function should return "Fizz". 
If the number is a multiple of  5, the function should return "Buzz". 
If the number is a multiple of both 3 and 5 return "FizzBuzz". 
If the number is not a multiple of either 3 or 5, return the number itself.

Example:

num = 20
Expected output = "Buzz"


"""


def fizzbuzz(num):
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    else:
        return num