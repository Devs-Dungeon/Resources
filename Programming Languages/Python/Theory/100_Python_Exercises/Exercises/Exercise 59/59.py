#Print out three lines saying for instance item 1 has index 0, and so on.
a = [1, 2, 3]

for index, item in enumerate(a):
    print("Item %s has index %s" % (item, index))
