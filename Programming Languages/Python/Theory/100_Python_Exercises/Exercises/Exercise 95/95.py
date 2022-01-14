#Create a program that asks the user to input values separated by commas and those values will be stored in a separate line each in a text file

line = input("Enter values: ")

line_list = line.split(",")

with open("user_data_commas.txt", "a+") as file:
    for i in line_list:
        file.write(i + "\n")

#Video question -Intermediate
