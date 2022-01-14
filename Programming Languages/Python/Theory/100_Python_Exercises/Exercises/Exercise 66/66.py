#Create a function that takes a word from user and translates it using a dictionary of three words
d = dict(weather = "clima", earth = "terra", rain = "chuva")
def vocabulary(word):
    return d[word]

word = input("Enter word: ")
print(vocabulary(word))
