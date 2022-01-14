#The following code prints Hello, checks if 2 is greater than 1 and then breaks the loop because 2 is actually greater than 1. Therefore Hi is not printed out. Please replace break with something else so that Hello is printed out repeatedly and Hi is never printed.


while True:
    print("Hello")
    if 2 > 1:
        continue
    print("Hi")
