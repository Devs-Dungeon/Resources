"""
Write a Python function to generate and return a dictionary that contains key, value pairs (from 1 to 10) in the form of (x, x*x).

Expected output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10:100}
"""

#Solution is:

def create_dict():
    new_dict = {}
    for i in range(1, 11):
        new_dict[i] = i*i
    return new_dict
        
