import random
import string

# Function to generate a random password
def generate_password(length):
    # Define character sets for different complexity levels
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on complexity
    if length < 4:
        charset = lower_letters
    elif length < 8:
        charset = lower_letters + digits
    else:
        charset = lower_letters + upper_letters + digits + special_characters

    # Generate the password
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

# Prompt the user for the desired password length
try:
    length = int(input("Enter the desired password length: "))
    
    if length <= 0:
        print("Password length must be a positive integer.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Invalid input. Please enter a valid positive integer for password length.")
