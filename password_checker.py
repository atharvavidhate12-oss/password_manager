import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 12:
        strength += 1
    else:
        feedback.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include numbers.")

    if re.search(r"[@$!%*#?&]", password):
        strength += 1
    else:
        feedback.append("Include special characters.")

    if strength == 5:
        return "Strong password ✔", feedback
    elif strength >= 3:
        return "Moderate password ⚠", feedback
    else:
        return "Weak password ❌", feedback
