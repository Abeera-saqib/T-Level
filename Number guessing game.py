import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.target_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Arial", 12))
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game, font=("Arial", 12))
        self.reset_button.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < 1 or guess > 100:
                self.result_label.config(text="Please guess a number between 1 and 100.")
            elif guess < self.target_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.target_number:
                self.result_label.config(text="Too high! Try agsin.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number {self.target_number} in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Invalid input! Please enter a number.")
    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
    
