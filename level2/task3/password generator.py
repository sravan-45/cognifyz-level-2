import re

def evaluate_password_strength(password):
    # Minimum length requirement
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    # Presence of uppercase and lowercase letters
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return "Weak: Password should contain both uppercase and lowercase letters."

    # Presence of digits
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."

    # Presence of special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>)."

    return "Strong: Password meets all strength criteria."

# Test the function
password = input("Enter your password: ")
strength = evaluate_password_strength(password)
print(strength)
