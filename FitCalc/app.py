import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert height from cm to meters
        bmi = weight / (height ** 2)
        bmi_rounded = round(bmi, 2)

        # Classify the BMI
        if bmi < 18.5:
            classification = "underweight"
        elif 18.5 <= bmi < 24.9:
            classification = "healthy"
        elif 25 <= bmi < 29.9:
            classification = "overweight"
        else:
            classification = "obese"

        result_label.config(text=f"Your BMI index is: {bmi_rounded}\nYou are classified as: {classification}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Function to clear inputs and results
def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

# Create a themed tkinter window
root = ThemedTk(theme="Breeze")
root.title("BMI Calculator")
root.geometry("300x300")  # Set appropriate window size

# Label for weight input
weight_label = ttk.Label(root, text="Enter your weight in kg:")
weight_label.pack(pady=5)

# Entry for weight
weight_entry = ttk.Entry(root)
weight_entry.pack(pady=5)

# Label for height input
height_label = ttk.Label(root, text="Enter your height in cm:")
height_label.pack(pady=5)

# Entry for height
height_entry = ttk.Entry(root)
height_entry.pack(pady=5)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=5)

# Result label
result_label = ttk.Label(root, text="", font=("Ubuntu", 12), justify='center')
result_label.pack(pady=10)

# Clear button
clear_button = ttk.Button(root, text="Clear", command=clear_fields)
clear_button.pack(pady=5)

# Run the application
root.mainloop()
