import random

# Prompt the user to enter the length
length = int(input("Enter the length of the password to generate : "))

# We manually define the possible characters the password can contain
upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special_characters = "!@#$%^&*()_+-=[]{};:,.<>?/|"

# Combine all character sets into one string
char = upper_case_letters + lower_case_letters + digits + special_characters

# Generate a random password by picking random characters from all_characters
password = ""

# Loop 'length' times to generate each character of the password
for i in range(length):
    password += random.choice(char)

# Output the randomly generated password
print("Your password is:", password)