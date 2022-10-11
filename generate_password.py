import tkinter as tk
import string
import random
def generate_unique_password():
    password = []
    for i in range(5):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        numbers = random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)
        passwords = " ".join(str(x)for x in password)
        label.config(text=passwords)
root = tk.Tk()
root.geometry("500x400")
root.title("Unique password generator")
button = tk.Button(root, text="Generate Password", command=generate_unique_password).place(x=200,y=200)
label = tk.Label(root, font=("times", 15, "bold"))
label.grid(row=4, column=2)
root.mainloop()