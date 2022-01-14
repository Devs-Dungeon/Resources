#Create a program that asks the user to submit text through a GUI

from tkinter import *

window = Tk()

file = open("user_gui.txt", "a+")

def add():
    file.write(user_value.get() + "\n")
    entry.delete(0, END)

def save():
    global file
    file.close()
    file = open("user_gui.txt", "a+")

def close():
    file.close
    window.destroy()

user_value = StringVar()
entry = Entry(window, textvariable=user_value)
entry.grid(row=0, column=0)

button_add = Button(window, text="Add line", command=add)
button_add.grid(row=0, column=1)

button_save = Button(window, text="Save changes", command=save)
button_save.grid(row=0, column=2)

button_close = Button(window, text="Save and Close", command=close)
button_close.grid(row=0,column=3)

window.mainloop()
