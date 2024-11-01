import random
import string 
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        output.config(text=password, font=("Ubuntu", 20), justify='center')
        copy_button.config(text="Copy", state="normal")  # Enable the copy button after generating a password
    except ValueError:
        output.config(text="Please enter a valid number", font=("Ubuntu", 12), justify='center')

# Function to copy the password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output.cget("text"))
    root.update()  # Keeps the clipboard active
    copy_button.config(text="Copied!", state="disabled")
    root.after(2000, reset_copy_button)  # Reset button after 2 seconds

# Function to reset the copy button text
def reset_copy_button():
    copy_button.config(text="Copy", state="normal")

# Create a themed tkinter window
root = ThemedTk(theme="yaru")
root.title("PASSKEY")
root.geometry("300x200")

# Label for input prompt
prompt_label = ttk.Label(root, text="Enter the length of the password:")
prompt_label.pack(pady=5)

# Entry for password length
length_entry = ttk.Entry(root)
length_entry.pack(pady=5)

# Output label for the password
output = ttk.Label(root, text="", font=("Ubuntu", 20), justify='center')
output.pack(pady=5)

# Generate button to generate the password
generate_button = ttk.Button(root, text="Generate", command=generate_password)
generate_button.pack(pady=5)

# Copy Button
copy_button = ttk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Run the application
root.mainloop()