import tkinter as tk
from tkinter import messagebox
import random
import time
import winsound

class MathsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maths App")
        self.root.geometry("400x400")
        
        self.score = 0
        self.level = 1
        self.timer = 60
        self.running = False

        self.create_widgets()
        self.generate_question()

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self.root, text="Maths App", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        # Score and Timer
        self.status_frame = tk.Frame(self.root)
        self.status_frame.pack()
        self.score_label = tk.Label(self.status_frame, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack(side="left", padx=10)
        self.timer_label = tk.Label(self.status_frame, text=f"Time: {self.timer}s", font=("Arial", 14))
        self.timer_label.pack(side="right", padx=10)

        # Question Label
        self.question_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        # Entry and Submit
        self.answer_entry = tk.Entry(self.root, font=("Arial", 14))
        self.answer_entry.pack(pady=10)
        self.submit_button = tk.Button(self.root, text="Submit", font=("Arial", 14), command=self.check_answer)
        self.submit_button.pack(pady=10)

    def start_timer(self):
        if self.running:
            if self.timer > 0:
                self.timer -= 1
                self.update_timer()
                self.root.after(1000, self.start_timer)
            else:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                messagebox.showinfo("Time's up!", "Time is up! Moving to the next question.")
                self.generate_question()

    def update_timer(self):
        self.timer_label.config(text=f"Time: {self.timer}s")
        if self.timer <= 10:
            self.timer_label.config(fg="red")
        else:
            self.timer_label.config(fg="black")

    def generate_question(self):
        self.running = True
        self.timer = 60
        self.update_timer()
        self.start_timer()

        num1 = random.randint(1, 10 * self.level)
        num2 = random.randint(1, 10 * self.level)
        self.correct_answer = num1 + num2
        self.question_label.config(text=f"{num1} + {num2} = ?")
        self.answer_entry.delete(0, tk.END)

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.correct_answer:
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                if self.score % 5 == 0:  # Increase level every 5 points
                    self.level += 1
                    messagebox.showinfo("Level Up!", f"Welcome to Level {self.level}!")
                self.generate_question()
            else:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                messagebox.showerror("Incorrect", "Try again!")
        except ValueError:
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            messagebox.showerror("Error", "Please enter a valid number.")

    def handle_close(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.root.destroy()

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = MathsApp(root)
    root.protocol("WM_DELETE_WINDOW", app.handle_close)
    root.mainloop()
