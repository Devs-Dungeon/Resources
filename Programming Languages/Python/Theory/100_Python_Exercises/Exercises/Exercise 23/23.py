#Access the third value of key b.
from pprint import pprint
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

pprint(d['b'][2])
