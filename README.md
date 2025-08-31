# Password Strength Analyser

A Python program that evaluates the strength of a password based on **length, character variety, entropy, and common passwords**. Provides a **detailed report** and rates the password as Weak, Fair, Strong, or Very Strong.

---

## Features

- Checks for **password length** and penalizes very short passwords.  
- Evaluates **character variety**: lowercase, uppercase, digits, and symbols.  
- Estimates **entropy** based on the number of unique characters.  
- Detects **common passwords** from a predefined list to immediately flag very weak passwords.  
- Provides a **score breakdown** and a final strength rating.

---

## Installation

1. Make sure you have **Python 3.x** installed.  
2. Clone or download this repository.  
3. Place the file `common-passwords.txt` in the same directory as `analyser.py`.  
   - This file should contain a list of common passwords, one per line.

---

## Usage

1. Open a terminal or command prompt.  
2. Navigate to the directory containing the script.  
3. Run the program:

```bash
python analyser.py
