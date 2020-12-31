import tkinter
from tkinter import messagebox
from random import randint

low = 0
high = 5
rand = randint(low, high)

def check(guess):
    if guess < rand:
        tkinter.messagebox.showinfo(f"Too low", "Wrong, number is too low!")
    elif guess > rand:
        tkinter.messagebox.showinfo(f"Too high", "Wrong, number is too high!")
    else:
        tkinter.messagebox.showinfo("Correct!", f"{guess} is correct")


tk = tkinter.Tk()
tk.title("Guessing game")

label = tkinter.Label(tk, text=f'Guess a number {low} to {high}')
label.pack()

entry = tkinter.Entry(tk)
entry.pack()

button = tkinter.Button(tk, text="Guess", command=lambda: check(int(entry.get())))
button.pack()

tk.mainloop()