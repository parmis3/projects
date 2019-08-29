# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")


E1 = Entry(top, bd = 5)
E1.place(x = 10,y = 10)

B = Button(top, text = "multiply 2", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()