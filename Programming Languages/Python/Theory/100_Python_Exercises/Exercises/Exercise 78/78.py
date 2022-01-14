#When writing web apps, you may need to generate default random passwords for users.
#Create a program that generates a password of 6 random alphanumeric characters in the range abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?

import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
chosen = random.sample(characters, 6)
password = "".join(chosen)
print(password)


#Video question -Easy
