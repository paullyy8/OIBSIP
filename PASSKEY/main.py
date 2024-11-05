import random
import string

# Welcome message
print("\nWelcome to PASSKEY! Your personal password generator.\n")

# Function to validate if input is an integer and within range
def get_valid_int(prompt, min_value=1):
    while True:
        try:
            value = int(input(f"{prompt:<35}: "))
            if value >= min_value:
                return value
            else:
                print(f"{'':<35}Please enter a number greater than or equal to {min_value}.")
        except ValueError:
            print(f"{'':<35}Invalid input. Please enter a valid integer.")

# Function to check password strength
def check_password_strength(password):
    length = len(password)
    if length < 8:
        return "Weak"
    elif length < 12:
        return "Moderate"
    else:
        return "Strong"

# Define character categories
upper_case_letters = string.ascii_uppercase
lower_case_letters = string.ascii_lowercase
digits = string.digits
special_characters = "!@#$%^&*()_+-=[]{};:,.<>?/|"

# Initialize password components
password_chars = ""
password = ""

# Ask if the user wants characters
need_characters = input(f"{'Do you need letters in your password?':<35} (Y/N): ").strip().upper()

if need_characters == "Y":
    # Allow for a range of characters
    num_characters = get_valid_int("How many letters would you like", min_value=1)
    password_chars += upper_case_letters + lower_case_letters
else:
    num_characters = 0

# Ask if the user wants symbols
include_symbols = input(f"{'Do you want symbols in your password?':<35} (Y/N): ").strip().upper()
if include_symbols == "Y":
    num_symbols = get_valid_int("How many symbols would you like", min_value=1)
    password_chars += special_characters
else:
    num_symbols = 0

# Ask if the user wants numbers
include_numbers = input(f"{'Do you want numbers in your password?':<35} (Y/N): ").strip().upper()
if include_numbers == "Y":
    num_numbers = get_valid_int("How many numbers would you like", min_value=1)
    password_chars += digits
else:
    num_numbers = 0

# Validate at least two types of characters are selected
if (num_characters == 0 and num_symbols == 0) or (num_characters == 0 and num_numbers == 0) or (num_symbols == 0 and num_numbers == 0):
    print("\nYou must select at least two types of characters to generate a secure password.")
else:
    # Generate the password
    password = ""
    for _ in range(num_characters):
        password += random.choice(upper_case_letters + lower_case_letters)

    for _ in range(num_symbols):
        password += random.choice(special_characters)

    for _ in range(num_numbers):
        password += random.choice(digits)

    # Shuffle the password to ensure randomness
    password = ''.join(random.sample(password, len(password)))

    # Provide feedback on the strength of the generated password
    password_strength = check_password_strength(password)

    # Output the randomly generated password with a box around it
    print("\n" + "-" * 50)
    print(f"Your Generated Password 🔑 is: {password}")
    print(f"The Password's Strength 💪 is: {password_strength}")
    print("-" * 50)

    print("\nMake sure to save it in a secure place! 💾\n")