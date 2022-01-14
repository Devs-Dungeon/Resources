#Write a function that calculates acceleration given the formula:
#a = (v2 - v1) / t2 - t1

def acceleration(v1, v2, t1, t2):
    a = float(v2 - v1) / float((t2 - t1))
    return a

print(acceleration(0,10,0,20))
