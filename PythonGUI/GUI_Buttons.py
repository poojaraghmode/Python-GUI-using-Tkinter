from tkinter import *

root = Tk()

def printname():
    print("Snehal Chodankar")
    label1 = Label(root, text = "SNEHAL CHODANKAR")
    label1.grid(row = 0, column = 1)

def printName(event):
    print("Pooja Raghmode")
    label2 = Label(root, text="POOJA RAGHMODE")
    label2.grid(row=1, column=1)

#There are two ways to interact with the functions using buttons.
button1 = Button(root, text = "Print my name1", command = printname)
button1.grid(row = 0, column = 0)

button2 = Button(root,text = "Print my name2")
button2.bind("<Button-1>", printName)
button2.grid(row = 1, column =0)

root.mainloop()