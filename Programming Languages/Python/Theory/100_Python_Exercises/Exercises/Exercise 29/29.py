#Write a function that calculates liquid formula taken from http://www.1728.org/spherprt.gif
#When writing the function consider that r is always 10.

from math import pi

def volume(h, r = 10):
    v = ((4 * pi * r**3) / 3) - (pi * h**2 * (3*r - h) / 3)
    return v

print(volume(2))
