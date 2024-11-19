from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title("Scientific calculator")
root.configure(background ="Powder blue")
root.resizable(width =False, height=False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label = "Standard")
filemenu.add_command(label = "Scientific")
filemenu.add_seperator()
filemenu.add_command(label = "Exit")


editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu=filemenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_seperator()
editmenu.add_command(label = "Paste")





root.config(menu=menubar)
root.mainloop()
