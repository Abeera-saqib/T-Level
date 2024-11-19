"""Ayman and his other friends planned to play cricket. They tossed a coin to decide between batting and balling. Ayman got an idea to create a virtual coin in python GUI programming. He created a GUI program with a button toss and each time he clicks the button he gets a random side of the coin. Create the same program and toss the coin."""

import tkinter as tk
import random 

def toss_coin():

    result = random.choice(['heads', 'tails'])
    result_label.config(text=result)

root = tk.Tk()
root.title("Virtual Coin Toss")

result_label = tk.Label(root ,text="" ,font=('Ariel', 24))
result_label.pack(pady=20)

toss_button = tk.Button(root ,text="Toss Coin", command=toss_coin)
toss_button.pack()

root.mainloop()
