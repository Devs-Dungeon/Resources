#Create a script that lets the user submit a password until they have satisfied three conditions:
#1. Password contains at least one number
#2. Contains one uppercase letter
#3. It is at least 5 chars long
#Print out message "Passowrd is not fine" if the user didn't create a correct password

while True:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
        print("Passowrd is not fine")
