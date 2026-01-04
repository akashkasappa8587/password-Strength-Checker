import re

def check_password_strength(password):
    """
    Checks the strength of a given password based on length and character diversity.

    Args:
        password (str): The password string to evaluate.

    Returns:
        tuple: A tuple containing (score_summary, detailed_feedback_list)
    """
    # 1. Initialize Score and Feedback
    score = 0
    feedback = []

    # Define standard character sets for checking
    min_length = 8
    
    # --- Check 1: Length ---
    if len(password) >= min_length:
        score += 2
        feedback.append(f"✓ Length: Excellent (Is {len(password)} characters long).")
    elif len(password) >= 6:
        score += 1
        feedback.append(f"★ Length: Good (Is {len(password)} characters long, consider aiming for 8+).")
    else:
        feedback.append(f"✗ Length: Weak (Only {len(password)} characters). Add {min_length - len(password)} more characters.")

    # --- Check 2: Uppercase Letters ---
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✓ Uppercase letters: Present.")
    else:
        feedback.append("✗ Uppercase letters: Missing. Add at least one (A-Z).")

    # --- Check 3: Lowercase Letters ---
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✓ Lowercase letters: Present.")
    else:
        feedback.append("✗ Lowercase letters: Missing. Add at least one (a-z).")

    # --- Check 4: Digits (Numbers) ---
    if re.search(r'\d', password):
        score += 1
        feedback.append("✓ Digits: Present.")
    else:
        feedback.append("✗ Digits: Missing. Add at least one number (0-9).")

    # --- Check 5: Special Characters ---
    # Common special characters: !@#$%^&*()-_+=
    if re.search(r'[!@#$%^&*()\-+=\[\]{}|;:,.<>?/~`]', password):
        score += 1
        feedback.append("✓ Special characters: Present.")
    else:
        feedback.append("✗ Special characters: Missing. Add at least one symbol (e.g., !@#$%).")

    # --- Determine Overall Strength ---
    
    strength = "Very Weak"
    color = "\033[91m" # Red
    
    if score >= 6:
        strength = "Very Strong"
        color = "\033[92m" # Green
    elif score >= 5:
        strength = "Strong"
        color = "\033[92m" # Green
    elif score >= 3:
        strength = "Medium"
        color = "\033[93m" # Yellow
    elif score >= 1:
        strength = "Weak"
        color = "\033[91m" # Red

    score_summary = f"{color}Overall Strength: {strength} (Score: {score}/6)\033[0m"

    return score_summary, feedback

if __name__ == "__main__":
    print("--- Password Strength Checker ---")
    print("Criteria: Length (8+), Uppercase, Lowercase, Digits, Special Characters.")
    
    # Get user input for password
    # NOTE: In a real-world application, do not print the password back to the console
    password_input = input("Enter a password to check: ")

    if not password_input:
        print("\nError: Password cannot be empty.")
    else:
        summary, details = check_password_strength(password_input)
        
        print("\n" + "="*30)
        print(summary)
        print("="*30)
        
        print("\nDetailed Feedback:")
        for line in details:
            print(line)

        print("\nTip: A stronger password should ideally achieve a score of 5 or 6.")