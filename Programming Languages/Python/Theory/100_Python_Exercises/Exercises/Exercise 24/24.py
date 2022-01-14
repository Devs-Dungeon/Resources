#Complete the script so it prints out the expected output

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

print(d.items())

for key, value in d.items():
    print(key, "has value", value)
