import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    username = name_entry.get()

    if username == "":
        messagebox.showerror("Error", "Please enter your name")
        return

    numbers = ''.join(random.choice(string.digits) for _ in range(2))
    symbols = ''.join(random.choice("!@#$%^&*") for _ in range(2))

    password = username + numbers + symbols

    result_label.config(
        text=f"Generated Password:\n{password}"
    )

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

tk.Label(root, text="Enter Your Name").pack(pady=10)

name_entry = tk.Entry(root)
name_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

root.mainloop()