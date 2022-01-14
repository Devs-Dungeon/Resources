#Create a script that gets user's age and returns year of birth
from datetime import datetime

age = int(input("What's your age? "))
year_birth = datetime.now().year - age
print("You were born back in %s" % year_birth)
