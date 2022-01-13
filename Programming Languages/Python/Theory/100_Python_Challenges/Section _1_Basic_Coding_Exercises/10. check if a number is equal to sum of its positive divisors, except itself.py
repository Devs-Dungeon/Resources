"""

Write a function that accepts a random number and checks if number is equal to the sum of its positive divisors, except itself.

Example:

Input num = 28

Expected output = True

"""


def sum_pos_divisor(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
        else:
            continue
    if sum == num:
        return True
    else:
        return False
        