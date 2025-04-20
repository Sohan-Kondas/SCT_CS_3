import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    errors = {
        "Too short (min 8 characters)": length_error,
        "Missing uppercase letter": uppercase_error,
        "Missing lowercase letter": lowercase_error,
        "Missing digit": digit_error,
        "Missing special character": special_char_error,
    }

    if all(not error for error in errors.values()):
        strength = "Strong 💪"
    elif sum(errors.values()) <= 2:
        strength = "Moderate 🔐"
    else:
        strength = "Weak ⚠️"

    return strength, [msg for msg, err in errors.items() if err]

# Example usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, issues = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if issues:
        print("Issues found:")
        for issue in issues:
            print(f" - {issue}")
    else:
        print("Your password is good to go! ✅")
