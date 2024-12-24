import re

# Check password strength
def check_password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r'[A-Z]', password): score += 1
    if re.search(r'[a-z]', password): score += 1
    if re.search(r'[0-9]', password): score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): score += 1

    print(f"Password Strength: {score}/5")
    if score < 3:
        print("Weak password! Use a mix of uppercase, lowercase, numbers, and symbols.")
    else:
        print("Strong password!")

# Main program
if __name__ == "__main__":
    print("=== Password Strength Analyzer ===")
    while True:
        password = input("Enter a password to analyze (or 'exit' to quit): ").strip()
        if password.lower() == "exit":
            break
        check_password_strength(password)
