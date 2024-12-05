import tkinter as tk
from tkinter import messagebox
import string

# Function to check password strength
def check_password_strength():
    password = password_entry.get()
    if not password:  # Handle empty password input
        messagebox.showinfo("Password Strength", "Please enter a password!")
        return

    strength = 0

    # Character type checks
    upper_case = any(c in string.ascii_uppercase for c in password)
    lower_case = any(c in string.ascii_lowercase for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c in string.digits for c in password)

    characters = [upper_case, lower_case, special, digits]
    length = len(password)
    score = 0

    # Length scoring
    if length >= 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1

    # Character diversity scoring
    if sum(characters) > 1:
        score += 1
    if sum(characters) > 2:
        score += 1
    if sum(characters) > 3:
        score += 1

    # Character type diversity scoring
    char_types = sum(characters)
    score += max(0, char_types - 1)

    # Final evaluation
    if score < 4:
        result = f"Password score: {score}/7 - Weak"
    elif score == 4:
        result = f"Password score: {score}/7 - Good"
    elif score > 4 and score < 6:
        result = f"Password score: {score}/7 - Pretty Good"
    else:
        result = f"Password score: {score}/7 - Excellent"

    # Display popup with the result
    messagebox.showinfo("Password Strength is:", result)

# GUI Window
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("400x200")

# GUI Layout
frame = tk.Frame(window, padx=10, pady=10)
frame.pack(pady=20)

# Password title label
title_label = tk.Label(frame, text="Please Enter Your Password:",font=("Times New Roman",11,"bold"),bg="grey",fg="white")
title_label.pack()

# Password entry field
password_entry = tk.Entry(frame, show="*", width=30)
password_entry.pack(pady=5)

# Password button
check_button = tk.Button(frame, text="Check Strength", command=check_password_strength,font=("Times New Roman",11,"bold"),bg="grey",fg="white")
check_button.pack(pady=10)

# Run application
window.mainloop()