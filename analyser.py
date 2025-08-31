# Password Strength Analyser
# Checks password length, character variety, entropy, and common password list
# Prints a detailed report with a strength rating

scores = {
    "length_score": 0,
    "variety_score": 0,
    "entropy": 0,
    "strength": ""
}

def main():
    """
    Main function to get user input and calculate password strength
    """
    totalScore = 0
    password = ""

    # Prompt user until a non-empty password is entered
    while password == "":
        password = input("Enter password: ")

    # Check if password is in common-password list
    if is_common(password):
        print("Your password is in the list of most common passwords! Very Weak.")
        return

    # Calculate total score
    totalScore = (
        check_password_length(password) +
        check_character_variety(password) +
        check_entropy(password)
    )

    # Print final report
    final_strength(totalScore)


def check_password_length(password):
    """
    Assigns a score based on password length.
    Penalizes passwords shorter than 8 characters.
    """
    length_score = 0

    if len(password) < 8:
        length_score = -20  # penalty for very short passwords
    elif len(password) < 10:
        length_score = 5
    elif len(password) < 12:
        length_score = 10
    elif len(password) < 16:
        length_score = 20
    else:
        length_score = 30

    scores["length_score"] = length_score
    return length_score


def check_character_variety(password):
    """
    Checks for the presence of lowercase, uppercase, digits, and symbols.
    Each type contributes 10 points to the variety score.
    """
    score = 0
    lower_check = False
    upper_check = False
    digit_check = False
    symbol_check = False
    checks = []

    # Iterate through each character to determine character types
    for letter in password:
        if letter.islower():
            lower_check = True
        if letter.isupper():
            upper_check = True
        if letter.isnumeric():
            digit_check = True
        if not letter.isalnum():
            symbol_check = True

    # Add all checks to a list
    checks.append(lower_check)
    checks.append(upper_check)
    checks.append(digit_check)
    checks.append(symbol_check)

    # Each True check contributes 10 points
    for check in checks:
        if check:
            score += 10

    scores["variety_score"] = score
    return score


def check_entropy(password):
    """
    Estimates password entropy based on unique characters.
    Scales the score to a maximum of 30.
    """
    letters_used = []
    unique = 0

    for letter in password:
        if letter not in letters_used:
            letters_used.append(letter)
            unique += 1

    ratio = unique / len(password)
    score = int(ratio * 30)

    scores["entropy"] = score
    return score


def is_common(password):
    """
    Checks if the password exists in the common-password list.
    Returns True if found, False otherwise.
    """
    with open("common-passwords.txt", "r") as file:
        passwordList = file.read().splitlines()
        if password in passwordList:
            return True
    return False


def final_strength(totalScore):
    """
    Determines overall password strength based on total score
    and prints a detailed report.
    """
    if totalScore <= 30:
        scores["strength"] = "Weak"
    elif totalScore <= 60:
        scores["strength"] = "Fair"
    elif totalScore <= 80:
        scores["strength"] = "Strong"
    else:
        scores["strength"] = "Very Strong"

    # Detailed report
    print("\n--- Password Report ---")
    print("Length Score:", scores["length_score"])
    print("Variety Score:", scores["variety_score"])
    print("Entropy Score:", scores["entropy"])
    print("Total:", totalScore)
    print("Final Strength:", scores["strength"])


# Run the password analyser
main()
