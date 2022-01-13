"""
Write a function to determine the factors of a number. Return the output in the form of a list.
Example:
input = 26
output = [1,2,13,26]
"""


def factors(num):
    output_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            output_list.append(i)
        else:
            break
    return (output_list)