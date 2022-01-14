#A: str and int  do not support a minus operand. It doesn't make sense to substract a text from a number or the other way around.
# change age-1 to int(age)-1
age = int(input("What's your age? "))
age_last_year = age - 1
print("Last year you were %s." % age_last_year)
