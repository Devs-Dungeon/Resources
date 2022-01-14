#Create a script that lets the user create a password until they have satisfied three conditions:
#Password contains at least one number, one uppercase letter and it is at least 5 chars long
#Give the exact reason why the user has not created a correct password
while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)

#Video question -Experienced
#Video solution -Experienced
