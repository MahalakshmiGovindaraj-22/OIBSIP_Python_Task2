import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return

        chars = ""

        if letters_var.get():
            chars += string.ascii_letters
        if numbers_var.get():
            chars += string.digits
        if symbols_var.get():
            chars += string.punctuation

        if chars == "":
            messagebox.showerror("Error", "Select at least one character type")
            return

        password = ""
        if letters_var.get():
            password += random.choice(string.ascii_letters)
        if numbers_var.get():
            password += random.choice(string.digits)
        if symbols_var.get():
            password += random.choice(string.punctuation)

        remaining = length - len(password)
        password += "".join(random.choice(chars) for _ in range(remaining))
        password = "".join(random.sample(password, len(password)))

        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
        if length < 6:
            strength_label.config(text="Strength: Weak", fg="red")
        elif length < 10:
            strength_label.config(text="Strength: Medium", fg="orange")
        else:
            strength_label.config(text="Strength: Strong", fg="green")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")


def copy_password():
    password = result_entry.get()
    if password == "":
        messagebox.showwarning("Warning", "No password to copy")
    else:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard")


def reset_fields():
    length_entry.delete(0, tk.END)
    result_entry.delete(0, tk.END)
    strength_label.config(text="")
    letters_var.set(False)
    numbers_var.set(False)
    symbols_var.set(False)

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("420x450")

tk.Label(root, text="Random Password Generator",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Password Length").pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

tk.Button(root, text="Generate Password",
          command=generate_password).pack(pady=10)

result_entry = tk.Entry(root, font=("Arial", 12), justify="center")
result_entry.pack(pady=10, ipadx=10)

strength_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
strength_label.pack(pady=5)

tk.Button(root, text="Copy Password",
          command=copy_password).pack(pady=5)

tk.Button(root, text="Reset",
          command=reset_fields).pack(pady=5)

root.mainloop()
