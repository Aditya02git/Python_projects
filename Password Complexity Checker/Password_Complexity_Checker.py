import re

def check_password_complexity(password):
    # Initialize feedback and score
    feedback = []
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1

    # Digit check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should include at least one digit.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    if score == 5:
        return "Strong password", feedback
    elif score >= 3:
        return "Moderate password", feedback
    else:
        return "Weak password", feedback

def main():
    print("Password Complexity Checker")
    print("===========================")
    password = input("Enter a password to check its complexity: ")
    strength, feedback = check_password_complexity(password)
    print(f"\nPassword strength: {strength}")
    if feedback:
        print("Feedback:")
        for f in feedback:
            print(f"- {f}")

if __name__ == "__main__":
    main()
