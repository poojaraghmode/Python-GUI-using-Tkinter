from tkinter import *

class classButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text = "Print message", command = self.printMessage)
        self.printButton.pack(side = LEFT)

        self.quitButton = Button(frame, text = "Quit", command = frame.quit)
        self.quitButton.pack(side = LEFT)

    def printMessage(self):
        print("Hello, GOOD to see you...")

root = Tk()
c = classButtons(root)
root.mainloop()