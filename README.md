Password Strength Analyzer

A Python program that evaluates the strength of a password based on length, character variety, entropy, and common passwords. Provides a detailed report and rates the password as Weak, Fair, Strong, or Very Strong.

Features

Checks for password length and penalizes very short passwords.

Evaluates character variety: lowercase, uppercase, digits, and symbols.

Estimates entropy based on the number of unique characters.

Detects common passwords from a predefined list to immediately flag very weak passwords.

Provides a score breakdown and a final strength rating.

Installation

Make sure you have Python 3.x installed.

Clone or download this repository.

Place the file common-passwords.txt in the same directory as analyzer.py.

This file should contain a list of common passwords, one per line.

Usage

Open a terminal or command prompt.

Navigate to the directory containing the script.

Run the program:

python analyzer.py


Enter a password when prompted.

The program will print a detailed password report, including:

Length Score

Variety Score

Entropy Score

Total Score

Final Strength

Example Output
Enter password: Abc123$%
--- Password Report ---
Length Score: 5
Variety Score: 40
Entropy Score: 30
Total: 75
Final Strength: Strong

How It Works

Length Score:

Passwords shorter than 8 characters are penalized.

Longer passwords earn more points.

Character Variety:

Points awarded for including lowercase, uppercase, digits, and symbols.

Entropy Score:

Measures the uniqueness of characters in the password.

Scaled to give stronger passwords higher points.

Common Password Check:

If the password exists in common-passwords.txt, it is flagged as Very Weak.

Future Improvements

Colorized CLI output for better visual feedback.

GUI interface using Tkinter or Streamlit.

Weight symbols higher for more realistic strength scoring.

Normalize case in common-password checks.

Optional scoring out of 100 for standardization.

License

This project is open-source and free to use.
