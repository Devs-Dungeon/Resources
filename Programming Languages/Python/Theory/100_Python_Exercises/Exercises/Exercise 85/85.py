#Create a script cleans the countries_raw.txt file from unecessary lines and leaves countries only

with open("countries_raw.txt", "r") as file:
    content = file.readlines()


content = [i.strip("\n") for i in content if "\n" in i]

content = [i for i in content if i !=""]
content = [i for i in content if i !="Top of Page"]

content = [i for i in content if len(i) != 1]
print(content)


with open("countries_clean.txt", "w") as file:
    for i in content:
        file.write(i+"\n")
