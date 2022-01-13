"""
Write a function that reads a given CSV file as a dictionary and returns the dictionary keys.

Input filename = 'input.csv'

Expected output = dict_keys(['Maths', 'Science', 'English'])


"""

#Solution is:

from csv import DictReader

def read_csv():
    with open('input.csv') as csvfile:
        csvreader = DictReader(csvfile)
        for row in csvreader:
            # process a row from the CSV file
            return row.keys()

        
        
