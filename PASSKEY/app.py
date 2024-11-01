import random
import string 
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

# Function to generate password
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(var.get()))
    output.config(text=password, font=("Ubuntu", 20), justify='center')

# Function to copy the password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output.cget("text"))
    root.update()  # Keeps the clipboard active
    copy_button.config(text="Copied!", state="disabled")

# Create a themed tkinter window
root = ThemedTk(theme="yaru")
root.title("PASSKEY")
root.geometry("300x200")

# GUI variables
var = tk.IntVar()
var.set(8)

# Drop Down menu to select the password length
dropdown = ttk.Combobox(root, textvariable=var, values=list(range(8, 21)))
dropdown.pack(pady=5)

# Generate button to generate the password
generate_button = ttk.Button(root, text="Generate", command=generate_password)
generate_button.pack(pady=5)

# Output label for the password
output = ttk.Label(root, text="", font=("Ubuntu", 20), justify='center')
output.pack(pady=5)

# Copy Button
copy_button = ttk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Run the application
root.mainloop()
