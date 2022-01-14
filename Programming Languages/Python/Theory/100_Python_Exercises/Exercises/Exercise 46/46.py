#Write a script that extracts letters from the 26 text files and put the letters in a list
import glob

letters = []
file_list = glob.glob("letters/*.txt")
print(file_list)
for filename in file_list:
    with open(filename, "r") as file:
        letters.append(file.read().strip("\n"))

print(letters)
