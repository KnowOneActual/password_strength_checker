import re


def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    if not re.search("[a-z]", password):
        return "Weak: Password must contain at least one lowercase letter."

    if not re.search("[A-Z]", password):
        return "Weak: Password must contain at least one uppercase letter."

    if not re.search("[0-9]", password):
        return "Weak: Password must contain at least one digit."

    if not re.search('[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password must contain at least one special character."

    return "Strong: Password is strong!"


# User input
user_password = input("Please enter your password to check its strength: ")
result = check_password_strength(user_password)
print(result)
