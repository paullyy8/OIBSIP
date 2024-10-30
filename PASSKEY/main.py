import random

# Welcome message
print("\n")
print("Welcome to PASSKEY!")

# Define possible characters
upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special_characters = "!@#$%^&*()_+-=[]{};:,.<>?/|"

# Initialize password components
password_chars = ""
password = ""

# Ask if the user wants characters
print("\n")
need_characters = input("Do you need characters in your password? (Y / N): ").strip().upper()

if need_characters == "Y":
    # Ask for the number of characters
    num_characters = int(input("How many characters would you like? : "))
    password_chars += upper_case_letters + lower_case_letters
else:
    num_characters = 0

# Ask if the user wants symbols
include_symbols = input("Do you want symbols in your password? (Y / N): ").strip().upper()
if include_symbols == "Y":
    # Ask for the number of symbols
    num_symbols = int(input("How many symbols would you like? : "))
    password_chars += special_characters
else:
    num_symbols = 0

# Ask if the user wants numbers
include_numbers = input("Do you want numbers in your password? (Y / N): ").strip().upper()
if include_numbers == "Y":
    # Ask for the number of numbers
    num_numbers = int(input("How many numbers would you like? : "))
    password_chars += digits
else:
    num_numbers = 0

# Check if at least two types are selected
if (num_characters == 0 and num_symbols == 0) or (num_characters == 0 and num_numbers == 0) or (num_symbols == 0 and num_numbers == 0):
    print("You must select at least two types of characters to generate a password.")
else:
    # Build the password
    for _ in range(num_characters):
        password += random.choice(upper_case_letters + lower_case_letters)

    for _ in range(num_symbols):
        password += random.choice(special_characters)

    for _ in range(num_numbers):
        password += random.choice(digits)

    # Shuffle the password to ensure randomness
    password = ''.join(random.sample(password, len(password)))

    # Output the randomly generated password with a box around it
    print("\n" + "-" * 50)
    print(f"Your generated password 🔑 is: {password}")
    print("-" * 50)
    print("\nMake sure to save it in a secure place! 💾")
    print("\n")
