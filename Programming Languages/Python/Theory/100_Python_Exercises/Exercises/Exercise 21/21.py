#Filter out values of equal or greater than 2
#Note that for Python 2 you will have to use iteritems
d = {"a": 1, "b": 2, "c": 3}
d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)
