"""
Write a function to find the longest common prefix string between a given set of strings. 
If there is no common prefix, return an empty string.

Example:

Input Data:

    s1 = 'floor'

    s2 = 'float'

    s3 = 'floral'

    s4 = 'flow'

Expected output = 'flo'
"""

def longest_prefix(s1,s2,s3,s4):
    arr = [s1, s2, s3, s4]
    if not arr:
        return ""
    elif len(arr) == 1:
        return arr[0]
    else:
        arr.sort()
        result = ""
        for i in range(len(arr[0])):
            if arr[0][i] == arr[-1][i]:
                result += arr[0][i]
            else:
                break
        return result
    
