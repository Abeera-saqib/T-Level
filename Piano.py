import tkinter as tk
from tkinter import messagebox
from playsound import playsound # pip install playsound==1.2.2
import os

# Play note function

def play_note(note):
    filename = f"{note}.wav"
    if os.path.exists(filename):
        playsound(filename)
    else:
        messagebox.showerror("Error",f"Audio file '{filename}' not found!")

# Create a main window

root = tk.Tk()
root.title("GUI Piano")

white_keys = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C1', 'D1', 'E1', 'F1']
black_keys = ['Cs', 'Ds', '', 'Fs', 'Gs', 'Bb', '', 'Cs1', 'Ds1']

# Dimensions

white_key_width = 60
white_key_height = 200
black_key_width = 40
black_key_height = 120

for i, key in enumerate(white_keys):    
    btn = tk.Button(root, text=key, bg='white', fg='black',
                    height = white_key_height // 20, width = white_key_width // 10,
                    command=lambda note=key: play_note(note))
    btn.place(x=i * white_key_width, y=0)

for i, key in enumerate(black_keys):
    if key:
        btn = tk.Button(root, text=key, bg='black', fg='white', height = black_key_height // 20, width = black_key_width // 10, command=lambda note=key: play_note(note))
        btn.place(x=(i * white_key_width) + (white_key_width - black_key_width // 2), y=0)

root.geometry(f"{len(white_keys) * white_key_width}x{white_key_height}")

root.mainloop()
