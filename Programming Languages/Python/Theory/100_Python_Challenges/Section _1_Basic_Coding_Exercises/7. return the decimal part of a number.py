"""
Write a function that returns the decimal part of a number. The output can be rounded to 2 decimal places.
If decimal part is zero, the function should return the string "INTEGER".

example 1:
num = 1.5
expected output = 0.50

example 2:
num = 2
expected output = "INTEGER"

"""



def decimal_part(num):
    nums = num - int(num)
    k = round(nums, 2)
    if nums == 0:
        return "INTEGER"
    else:
        return k