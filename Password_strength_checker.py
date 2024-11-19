import random
import string

def check_password_strength(password):
    """Checks the strength of the password."""
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."
    if not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."
    if not any(char in string.punctuation for char in password):
        return "Weak: Password must contain at least one special character."
    return "Strong"

def generate_password():
    """Generates a strong password."""
    length = 12  # Default password length
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    while True:
        password = input("Enter your password: ")
        strength = check_password_strength(password)
        print(f"Password Strength: {strength}")
        
        if "Weak" in strength:
            choice = input("Do you want the system to generate a strong password for you? (yes/no): ").strip().lower()
            if choice == 'yes':
                strong_password = generate_password()
                print(f"Generated Password: {strong_password}")
            else:
                print("Please try creating a stronger password!")
        else:
            print("Your password is strong. Good job!")
            break

if __name__ == "__main__":
    main()
