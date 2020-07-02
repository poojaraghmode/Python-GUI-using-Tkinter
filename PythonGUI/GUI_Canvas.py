from tkinter import *

root = Tk()

canvas = Canvas(root, width = 400, height = 300)
canvas.pack()

blackLine = canvas.create_line(0,0,200,50,fill = "red")
redline = canvas.create_line(0,100,200,50,fill = "black")

greenBox = canvas.create_rectangle(25,25,100,100, fill="green")

#canvas.delete(redline)
#canvas.delete(ALL)

root.mainloop()