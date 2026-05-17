# ============================================
# Password Generator Project
# Author: N.Durga prasad
# Date: 17/05/2026 
# Description: A GUI-based password generator
#              built with Python and Tkinter
# ============================================

import tkinter as tk
from tkinter import messagebox
import random
import string


# ---- All the characters we can use in passwords ----
UPPERCASE   = string.ascii_uppercase   # A-Z
LOWERCASE   = string.ascii_lowercase   # a-z
DIGITS      = string.digits            # 0-9
SPECIAL     = "!@#$%^&*()-_=+[]{}?><"  # special chars


# ---- Function to generate the password ----
def generate_password():
    # Get what the user typed in the length box
    length_input = length_entry.get().strip()

    # Make sure the user actually typed something
    if length_input == "":
        messagebox.showwarning("Missing Input", "Please enter a password length.")
        return

    # Make sure it's a number
    if not length_input.isdigit():
        messagebox.showerror("Invalid Input", "Password length must be a number.")
        return

    length = int(length_input)

    # Password should be at least 6 characters to be useful
    if length < 6:
        messagebox.showwarning("Too Short", "Please enter a length of at least 6.")
        return

    # Max limit just to keep things reasonable
    if length > 100:
        messagebox.showwarning("Too Long", "Please enter a length of 100 or less.")
        return

    # Make sure the password has at least one of each character type
    # This way the password is always strong
    password_chars = [
        random.choice(UPPERCASE),
        random.choice(LOWERCASE),
        random.choice(DIGITS),
        random.choice(SPECIAL),
    ]

    # Fill the rest of the password with random characters from everything
    all_chars = UPPERCASE + LOWERCASE + DIGITS + SPECIAL
    for i in range(length - 4):
        password_chars.append(random.choice(all_chars))

    # Shuffle so the first 4 characters aren't always predictable
    random.shuffle(password_chars)

    # Join the list into one string
    final_password = "".join(password_chars)

    # Show the password in the result box
    password_var.set(final_password)

    # Update the strength label based on length
    update_strength_label(length)


# ---- Function to copy password to clipboard ----
def copy_to_clipboard():
    password = password_var.get()

    # Don't copy if there's no password yet
    if password == "" or password == "Your password will appear here":
        messagebox.showinfo("Nothing to Copy", "Please generate a password first.")
        return

    # Clear the clipboard and add our password
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()  # needed to keep it in clipboard after window closes

    # Change button text briefly to give feedback
    copy_btn.config(text="✔  Copied!")
    window.after(2000, lambda: copy_btn.config(text="📋  Copy Password"))


# ---- Function to show password strength ----
def update_strength_label(length):
    if length < 8:
        strength_label.config(text="Strength: Weak 🔴", fg="#e74c3c")
    elif length < 12:
        strength_label.config(text="Strength: Medium 🟡", fg="#e67e22")
    elif length < 16:
        strength_label.config(text="Strength: Strong 🟢", fg="#27ae60")
    else:
        strength_label.config(text="Strength: Very Strong 💪", fg="#1abc9c")


# ---- Function to clear everything ----
def clear_all():
    length_entry.delete(0, tk.END)
    password_var.set("")
    password_display.config(fg="#aaaaaa")
    strength_label.config(text="Strength: ---", fg="#888888")
    copy_btn.config(text="📋  Copy Password")


# ============================================
#              BUILD THE WINDOW
# ============================================

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("480x520")
window.resizable(False, False)
window.configure(bg="#1e1e2e")  # dark background

# ---- App Title ----
title_label = tk.Label(
    window,
    text="🔐 Password Generator",
    font=("Segoe UI", 20, "bold"),
    bg="#1e1e2e",
    fg="#cdd6f4"
)
title_label.pack(pady=(30, 5))

# Small subtitle
subtitle_label = tk.Label(
    window,
    text="Generate strong & secure passwords instantly",
    font=("Segoe UI", 10),
    bg="#1e1e2e",
    fg="#6c7086"
)
subtitle_label.pack(pady=(0, 25))

# ---- Card Frame (the white-ish box in the middle) ----
card = tk.Frame(window, bg="#2a2a3e", bd=0, relief="flat")
card.pack(padx=35, pady=5, fill="both", expand=True)

# ---- Password Length Section ----
length_label = tk.Label(
    card,
    text="Password Length",
    font=("Segoe UI", 11, "bold"),
    bg="#2a2a3e",
    fg="#cdd6f4"
)
length_label.pack(anchor="w", padx=25, pady=(25, 5))

# Input field for length
length_entry = tk.Entry(
    card,
    font=("Segoe UI", 13),
    bg="#313145",
    fg="#cdd6f4",
    insertbackground="#cdd6f4",   # cursor color
    relief="flat",
    bd=0,
    justify="center",
    width=10
)
length_entry.pack(ipady=8, padx=25, fill="x")
length_entry.insert(0, "12")  # default value

# ---- Generate Button ----
generate_btn = tk.Button(
    card,
    text="⚡  Generate Password",
    font=("Segoe UI", 12, "bold"),
    bg="#7c3aed",       # purple
    fg="white",
    activebackground="#6d28d9",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2",
    command=generate_password
)
generate_btn.pack(pady=(18, 10), padx=25, fill="x", ipady=10)

# ---- Divider Line ----
divider = tk.Frame(card, bg="#3b3b52", height=1)
divider.pack(fill="x", padx=25, pady=(5, 15))

# ---- Generated Password Display ----
pass_title = tk.Label(
    card,
    text="Generated Password",
    font=("Segoe UI", 11, "bold"),
    bg="#2a2a3e",
    fg="#cdd6f4"
)
pass_title.pack(anchor="w", padx=25, pady=(0, 5))

# This variable holds the current password text
password_var = tk.StringVar()

# The password text box (read-only style)
password_display = tk.Entry(
    card,
    textvariable=password_var,
    font=("Courier New", 13),   # monospace font looks nice for passwords
    bg="#313145",
    fg="#a6e3a1",               # green text for the password
    insertbackground="#a6e3a1",
    relief="flat",
    bd=0,
    justify="center",
    state="readonly"            # user can't type here, only copy
)
password_display.pack(ipady=10, padx=25, fill="x")

# ---- Strength Label ----
strength_label = tk.Label(
    card,
    text="Strength: ---",
    font=("Segoe UI", 10),
    bg="#2a2a3e",
    fg="#888888"
)
strength_label.pack(pady=(10, 5))

# ---- Copy Button ----
copy_btn = tk.Button(
    card,
    text="📋  Copy Password",
    font=("Segoe UI", 11),
    bg="#059669",       # green
    fg="white",
    activebackground="#047857",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2",
    command=copy_to_clipboard
)
copy_btn.pack(pady=(5, 10), padx=25, fill="x", ipady=8)

# ---- Clear Button ----
clear_btn = tk.Button(
    card,
    text="🗑  Clear",
    font=("Segoe UI", 10),
    bg="#2a2a3e",
    fg="#6c7086",
    activebackground="#313145",
    activeforeground="#cdd6f4",
    relief="flat",
    bd=0,
    cursor="hand2",
    command=clear_all
)
clear_btn.pack(pady=(0, 20))

# ---- Footer ----
footer = tk.Label(
    window,
    text="Made with ❤️ using Python & Tkinter",
    font=("Segoe UI", 9),
    bg="#1e1e2e",
    fg="#45475a"
)
footer.pack(pady=(5, 15))

# ---- Start the app ----
window.mainloop()