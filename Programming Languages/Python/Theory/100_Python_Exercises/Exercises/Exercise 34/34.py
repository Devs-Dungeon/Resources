#The script throws an error (when global c is not there). Fix it so that the script prints the value assigned to c inside the function
#A: Add "global c" before "c=1".
#C: Worth mentioning that if you remove foo(), variable c will come as undifined because the function has not been run
def foo():
    #global c
    c = 1
    return c
foo()
print(c)
