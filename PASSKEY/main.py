import random

# Prompt the user to enter the length
length = int(input("\n" "Enter the desired length for your password: "))

# Define the possible characters the password can contain
upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special_characters = "!@#$%^&*()_+-=[]{};:,.<>?/|"

# Combine all character sets into one string
char = upper_case_letters + lower_case_letters + digits + special_characters

# Generate a random password by picking random characters from all_characters
password = ""

# Loop to generate each character of the password
for i in range(length):
    password += random.choice(char)

# Output the randomly generated password with a box around it
print("\n" + "-" * 50)
print(f"Your generated password is 🔑 : {password}")
print("-" * 50)
print("\nMake sure to save it in a secure place! 💾")