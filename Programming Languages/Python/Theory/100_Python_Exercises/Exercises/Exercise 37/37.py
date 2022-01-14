#Create a function like in the previous exercise, but taking into consideration that commas without space can separate words.
def count_words(filepath):
    with open(filepath, 'r') as file:
        string = file.read()
        string = string.replace(",", " ")
        string_list = string.split(" ")
        return len(string_list)

print(count_words("words2.txt"))

#Other solution using regular expressions
import re

def count_words_re(filepath):
    with open(filepath, 'r') as file:
        string = file.read()
        string_list = re.split(",| ", string)
        return len(string_list)

print(count_words_re("words2.txt"))
