#Create a script that generates 26 text files, each containing one letter of English alphabet as a name and as text inside.

import string, os

if not os.path.exists("letters"):
    os.makedirs("letters")
for letter in string.ascii_lowercase:
    with open("letters/" + letter + ".txt", "w") as file:
        file.write(letter + "\n")
