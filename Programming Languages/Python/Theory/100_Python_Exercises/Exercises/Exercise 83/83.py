#Write a script that detects and prints out your monitor resolution
from screeninfo import get_monitors
print(get_monitors())

width=get_monitors()[0].width
height=get_monitors()[0].height

print("Width: %s,  Height: %s" % (width, height))
