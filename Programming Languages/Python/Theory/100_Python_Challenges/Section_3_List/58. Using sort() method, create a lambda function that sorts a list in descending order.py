"""
Using sort() method, create a lambda function that sorts a list in descending order. 
Please avoid using the reverse parameter.
"""

def sort_dec(input_list):   

    input_list.sort()

    b=[]

    while True:

        if input_list==[]:

            break

        else:

            a=input_list.pop()

            b.append(a)

    return b