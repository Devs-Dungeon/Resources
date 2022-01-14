#Create a program that asks the user to submit text repeatedly
#The program closes when the user submits CLOSE

file = open("user_data.txt", 'a+')

while True:
    line = input("Write a value: ")
    if line == "CLOSE":
        file.close()
        break
    else:
        file.write(line + "\n")
