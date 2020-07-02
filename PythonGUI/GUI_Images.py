from tkinter import *
from PIL import ImageTk,Image

root = Tk()

myImg = ImageTk.PhotoImage(Image.open("PoojaRaghmode.jpg"))
myLabel = Label(image = myImg)
myLabel.pack()

root.mainloop()