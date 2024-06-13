import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("500x400")
        self.root.configure(bg="#e0f7fa")

        self.random_number = random.randint(1, 100)
        self.attempts = 0

        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.root, text="Guess the number between 1 and 100", font=("Helvetica", 20, "bold"), bg="#e0f7fa")
        self.label.pack(pady=20)

        self.entry_frame = tk.Frame(self.root, bg="#e0f7fa")
        self.entry_frame.pack(pady=10)
        
        self.entry_label = tk.Label(self.entry_frame, text="Your guess:", font=("Helvetica", 16), bg="#e0f7fa")
        self.entry_label.pack(side=tk.LEFT, padx=10)
        
        self.entry = tk.Entry(self.entry_frame, font=("Helvetica", 16), width=10)
        self.entry.pack(side=tk.LEFT, padx=10)

        self.button = tk.Button(self.root, text="Guess", command=self.check_guess, font=("Helvetica", 16, "bold"), bg="#00695c", fg="white", activebackground="#004d40", activeforeground="white")
        self.button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 18), bg="#e0f7fa")
        self.result_label.pack(pady=20)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game, font=("Helvetica", 14, "bold"), bg="#ff1744", fg="white", activebackground="#d50000", activeforeground="white")
        self.reset_button.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < 1 or guess > 100:
                self.result_label.config(text="Please enter a number between 1 and 100")
            elif guess < self.random_number:
                self.result_label.config(text="Too low! Try again.", fg="#d32f2f")
            elif guess > self.random_number:
                self.result_label.config(text="Too high! Try again.", fg="#d32f2f")
            else:
                self.result_label.config(text=f"Correct! You guessed it in {self.attempts} attempts.", fg="#388e3c")
                self.entry.config(state=tk.DISABLED)
                self.button.config(state=tk.DISABLED)

        except ValueError:
            self.result_label.config(text="Please enter a valid number", fg="#d32f2f")

    def reset_game(self):
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.entry.config(state=tk.NORMAL)
        self.button.config(state=tk.NORMAL)
        self.result_label.config(text="", fg="#000000")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
