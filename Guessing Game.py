import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        self.master.geometry("350x130")

        self.num = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Enter your guess:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)  

        self.btn = tk.Button(master, text="Guess", command=self.guessNum)
        self.btn.pack(pady=5)

    def guessNum(self):
        try:
            userNum = int(self.entry.get())
            self.attempts += 1

            if userNum < self.num:
                resultMsg = f"Too low! Try again. Attempts: {self.attempts}"
            elif userNum > self.num:
                resultMsg = f"Too high! Try again. Attempts: {self.attempts}"
            else:
                resultMsg = f"Congratulations!! \nYou've guessed the number {self.num} in:\n {self.attempts} attempts!"
                self.btn["state"] = "disabled"  

            self.label.config(text=resultMsg)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    game_gui = GuessingGame(root)
    root.mainloop()
