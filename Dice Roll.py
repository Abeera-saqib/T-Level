import tkinter as tk
from tkinter import Label, Button
import random
def roll_dice():
    random_number = random.randint(1,6)
    label.config(text=str(random_number))
root = tk.Tk()
root.title("Dice Roller")
label = Label(root, font=('Helvetica' , 100), width=3)
label.pack(pady=20)
button = Button(root, text="Roll Dice", command=roll_dice, font = ('Helvetica', 20))
button.pack(pady=10)
root.mainloop()
