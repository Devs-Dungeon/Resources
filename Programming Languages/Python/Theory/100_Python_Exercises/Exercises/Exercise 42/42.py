#Print out in each line the sum of homologous items from the two sequences

a = [1, 2, 3]
b = (4, 5, 6)

for i, j in zip(a, b):
    print(i + j)
