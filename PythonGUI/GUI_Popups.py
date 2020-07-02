from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Ttile', 'Window text...')

answer = tkinter.messagebox.askquestion('Question 1', 'Do u like to sing...?')
if answer == 'yes':
    print('Singer')
else:
    print('Fool')

root.mainloop()