import random
import string

def evaluate_password_strength(password):
    """Evaluate the strength of the generated password."""
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 8 and ((has_upper + has_lower + has_digit + has_special) >= 3):
        return "Moderate"
    else:
        return "Weak"

def generate_password_from_details(info_pool, min_length, numbers=True, special_characters=True):
    """Generate a password based on user details and preferences."""
    letters = string.ascii_letters
    digits = string.digits if numbers else ""
    special = string.punctuation if special_characters else ""

    # Combine pools
    char_pool = letters + digits + special
    if not char_pool:
        raise ValueError("No character pool available for password generation.")

    # Ensure the password meets the minimum length
    password = random.sample(info_pool, min(len(info_pool), min_length)) if info_pool else ""
    
    while len(password) < min_length:
        password += random.choice(char_pool)

    # Shuffle the password for randomness
    password = ''.join(random.sample(password, len(password)))
    return password

# User input
while True:
    try:
        min_length = int(input("Enter the minimum password length (minimum 8, maximum 64): "))
        if min_length < 8 or min_length > 64:
            print("Password length must be between 8 and 64. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

has_number = input("Do you want to include numbers in the password (y/n)? ").strip().lower() == "y"
has_special = input("Do you want to include special characters in the password (y/n)? ").strip().lower() == "y"

# Initialize info pool
info_pool = ""

include_name = input("Do you want to include your name in the password (y/n)? ").strip().lower() == "y"
if include_name:
    name = input("Enter your name: ").strip()
    info_pool += name

include_birthdate = input("Do you want to include your birthdate in the password (y/n)? ").strip().lower() == "y"
if include_birthdate:
    birthdate = input("Enter your birthdate (DD-MM-YYYY): ").strip()
    info_pool += birthdate

include_favorite_word = input("Do you want to include your favorite word in the password (y/n)? ").strip().lower() == "y"
if include_favorite_word:
    favorite_word = input("Enter your favorite word: ").strip()
    info_pool += favorite_word

if not info_pool:
    print("No personal details provided. Generating a password using default characters.")

try:
    pwd = generate_password_from_details(info_pool, min_length, has_number, has_special)
    strength = evaluate_password_strength(pwd)
    print(f"\nGenerated Password: {pwd}")
    print(f"Password Strength: {strength}")

    if strength != "Strong":
        print("Tip: Use a longer password with a mix of uppercase, lowercase, numbers, and special characters for better security.")
except ValueError as e:
    print(f"Error: {e}")
