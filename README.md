🛡️ Password Security Checker

A beginner-friendly cybersecurity project built in Python that evaluates password strength, detects weak patterns, calculates entropy, and helps users generate secure passwords. Designed as a perfect starter project for anyone entering the cybersecurity field.

🚀 Features

✔ Password Strength Scoring (weak → strong)
✔ Entropy Calculation
✔ Detection of Common Patterns
✔ Weak Password Alerts
✔ Secure Password Generator
✔ Simple & Clean Python Codebase
✔ Ideal for beginners learning cybersecurity

📂 Project Structure
password-security-checker/
│── main.py
│── utils/
│     ├── strength_checker.py
│     ├── entropy_calculator.py
│     ├── password_generator.py
│── requirements.txt
│── README.md
│── .gitignore

🛠️ Installation & Setup
1. Clone the repository
git clone https://github.com/yourusername/password-security-checker.git
cd password-security-checker

2. Install dependencies
pip install -r requirements.txt

3. Run the program
python main.py

📝 How It Works

This tool analyzes a password on multiple factors:

🔸 Length Score

Longer passwords get higher strength values.

🔸 Character Diversity

Checks for:

Uppercase letters

Lowercase letters

Numbers

Special characters

🔸 Weak Pattern Detection

Warns if the password contains:

Common words

Keyboard sequences (ex: qwerty)

Repeated characters

Reused patterns

🔸 Entropy Calculation

Entropy = how unpredictable the password is.
Higher entropy → more secure password.

🔸 Secure Password Generator

Generates strong, random passwords using:

Letters

Numbers

Special characters

You can customize length and complexity.

🧪 Example Output
Enter a password: MyPass123!
Strength: Strong
Entropy: 35.7 bits
Warnings:
- Avoid using dictionary-like words.
Suggested Strong Password:
t&F8!pmW#2

📦 Requirements
Python 3.8+
Packages listed in requirements.txt

🎯 Learning Objectives
This project helps you understand:

Secure coding fundamentals

Basic cryptography concepts

Entropy and password security

Cybersecurity mindset

Python scripting for security tools

Perfect if you're starting cybersecurity through projects.

🤝 Contributing
Pull requests are welcome!
If you have ideas for improvements, feel free to open an issue.

⭐ Support
If you found this helpful, consider giving the repository a star on GitHub!
