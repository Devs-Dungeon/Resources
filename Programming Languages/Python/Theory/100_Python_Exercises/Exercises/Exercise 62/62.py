#Create a program that prints Hello repeteadly after 1 second first, then after 2, 3, 4 increasing the interval by one
import time

i = 0
while True:
    print("Hello")
    i = i + 1
    time.sleep(i)
