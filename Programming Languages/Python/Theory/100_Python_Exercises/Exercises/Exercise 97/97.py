#Create a program that asks the user to submit text through a GUI

file = open("user_data_save_close.txt", 'a+')

while True:
    line = input("Write a value: ")
    if line == "SAVE":
        file.close()
        file = open("user_data_save_close.txt", 'a+')
    elif line == "CLOSE":
        file.close()
        break
    else:
        file.write(line + "\n")
