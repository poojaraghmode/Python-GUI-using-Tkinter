from tkinter import *
#Line 3 is just to create a blank window
root = Tk()
#Line 5 creates a label but does not display it
theLabel = Label(root, text = "This is too easy")
#Line 7 is used to display the Label that was created into the root window
theLabel.pack()
#Line 9 is used to keep running the GUI aapplication for infinite amount of time until the close button is pressed to stop it
root.mainloop()