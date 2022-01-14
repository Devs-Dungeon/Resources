#The script generates an error. Please add the appropriate code that adds variables a and b without an error.
#A: The script generates an error saying that an integer object cannot convert to string implicitly.
#Please try to convert the integer to a string explicitly then or the string to an integer.
a = "1"
b = 2
print(a + b)    # it throws an error

print(int(a) + b)    #it is the right syntax
