'''
Write a function that deletes all elements in set1 that exists only in set1 but not in set2.

set1 = {1,2,3,4,5}

set2 = {4,5,6,7,8}

'''

def diff_update(set1,set2):
    for elem in set2:
        if elem not in set1:
            pass
        else:
            set1.discard(elem)
    return set1