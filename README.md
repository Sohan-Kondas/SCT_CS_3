# Password Strength Assessment Tool

This repository contains a Python program that assesses the strength of a given password based on several common criteria. This was my third task as a Cyber Security Intern at SkillCraft Technology.

## Overview

The goal of this tool is to provide a basic evaluation of password strength by checking for the presence of different character types and the overall length. It considers the following factors:

-   **Length:** Longer passwords generally offer more security.
-   **Uppercase Letters:** Inclusion of uppercase letters increases complexity.
-   **Lowercase Letters:** Presence of lowercase letters is essential.
-   **Numbers:** Digits add to the randomness of a password.
-   **Special Characters:** Symbols further enhance password strength.

The tool assigns a basic strength level based on the combination of these factors.

## How to Use

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository_url>
    cd password-strength-checker
    ```

2.  **Run the Python script:**
    ```bash
    python password_checker.py
    ```

3.  **Enter the password** when prompted.

4.  **The program will output an assessment of the password's strength** along with feedback on the criteria met.

## Strength Assessment Criteria (Simplified)

The tool uses a simple scoring system based on the following:

-   **Length:** A higher score is awarded for longer passwords.
-   **Character Types:** Points are given for the presence of each of the following:
    -   Uppercase letters (A-Z)
    -   Lowercase letters (a-z)
    -   Numbers (0-9)
    -   Special characters (e.g., !, @, #, $, %, etc.)

The final strength assessment (e.g., Weak, Moderate, Strong) is a qualitative evaluation based on the total score.

## Example Usage

Enter your password: P@$$wOrd123
Password Strength: Strong
Feedback:

Password length is good.
Contains uppercase letters.
Contains lowercase letters.
Contains numbers.
Contains special characters.

Enter your password: password
Password Strength: Weak
Feedback:

Password length is short.
Contains only lowercase letters.
Does not contain numbers.
Does not contain special characters.

## Further Improvements

This is a basic password strength assessment tool. Potential enhancements could include:

-   Implementing more sophisticated scoring algorithms (e.g., considering character repetition, sequential characters, common patterns).
-   Providing more detailed feedback and recommendations for improvement.
-   Integrating with password generation tools.
-   Adding a graphical user interface (GUI).

## Author

Sohan Kondas

This project was completed as part of my Cyber Security Internship at SkillCraft Technology.
