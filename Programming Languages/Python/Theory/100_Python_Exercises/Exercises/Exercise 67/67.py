#Like the previous exercise, but returning a message when the word is not in the dict.
d = dict(weather = "clima", earth = "terra", rain = "chuva")
def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "That word does not exist."

word = input("Enter word: ")
print(vocabulary(word))
