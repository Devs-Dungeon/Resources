"""
Write a Python function to sort (ascending) a dictionary by value.

input_dict = {'apples':10,'oranges':6,'banana':12,'pears':5}

sorted_dict = {'pears': 5, 'oranges': 6, 'apples': 10, 'banana': 12}
"""

#Solution is:

def dict_sort(input_dict):
    return dict(sorted(input_dict.items(), key=lambda item: item[1]))
        
