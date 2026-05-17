# ============================================
# Rock Paper Scissors Game
# Author: [Your Name]
# Date: May 2026
# Description: A fun GUI-based Rock Paper
#              Scissors game using Tkinter
# ============================================

import tkinter as tk
from tkinter import font as tkfont
import random


# ---- Choices and their emoji icons ----
CHOICES = ["Rock", "Paper", "Scissors"]

EMOJI = {
    "Rock":     "🪨",
    "Paper":    "📄",
    "Scissors": "✂️"
}

# ---- Who beats who (player_choice beats ...) ----
WINS_AGAINST = {
    "Rock":     "Scissors",
    "Paper":    "Rock",
    "Scissors": "Paper"
}


# ---- Score tracking (starts at 0) ----
player_score = 0
computer_score = 0
ties = 0


# ---- Function to get computer's choice ----
def computer_pick():
    return random.choice(CHOICES)


# ---- Function to find out who won ----
def get_result(player, computer):
    if player == computer:
        return "tie"
    elif WINS_AGAINST[player] == computer:
        return "win"
    else:
        return "lose"


# ---- Main function that runs when a button is clicked ----
def play(player_choice):
    global player_score, computer_score, ties

    # Get computer's random choice
    comp_choice = computer_pick()

    # Find out who won
    result = get_result(player_choice, comp_choice)

    # Update scores based on result
    if result == "win":
        player_score += 1
        result_text   = "🎉  You Win!"
        result_color  = "#a6e3a1"   # green
        bg_flash      = "#1a3a2a"   # dark green flash

    elif result == "lose":
        computer_score += 1
        result_text    = "💻  Computer Wins!"
        result_color   = "#f38ba8"  # red
        bg_flash       = "#3a1a1a"  # dark red flash

    else:
        ties += 1
        result_text  = "🤝  It's a Tie!"
        result_color = "#f9e2af"    # yellow
        bg_flash     = "#2a2a1a"    # dark yellow flash

    # ---- Update all the labels on screen ----

    # Player choice display
    player_choice_label.config(
        text=f"{EMOJI[player_choice]}\n{player_choice}"
    )

    # Computer choice display
    computer_choice_label.config(
        text=f"{EMOJI[comp_choice]}\n{comp_choice}"
    )

    # Result message
    result_label.config(text=result_text, fg=result_color)

    # Score display
    score_label.config(
        text=f"You: {player_score}     Ties: {ties}     Computer: {computer_score}"
    )

    # Flash the result card background for visual feedback
    result_card.config(bg=bg_flash)
    window.after(400, lambda: result_card.config(bg="#2a2a3e"))

    # Also animate the vs section briefly
    vs_label.config(fg=result_color)
    window.after(600, lambda: vs_label.config(fg="#585b70"))


# ---- Function to reset the entire game ----
def reset_game():
    global player_score, computer_score, ties

    # Reset all scores to zero
    player_score   = 0
    computer_score = 0
    ties           = 0

    # Clear everything on screen
    player_choice_label.config(text="❓\nYour Choice")
    computer_choice_label.config(text="❓\nComputer")
    result_label.config(text="Make your move!", fg="#6c7086")
    score_label.config(text="You: 0     Ties: 0     Computer: 0")
    vs_label.config(fg="#585b70")


# ============================================
#              BUILD THE WINDOW
# ============================================

# Create main window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("520x660")
window.resizable(False, False)
window.configure(bg="#1e1e2e")

# ---- Title at the top ----
title_label = tk.Label(
    window,
    text="Rock  Paper  Scissors",
    font=("Segoe UI", 20, "bold"),
    bg="#1e1e2e",
    fg="#cdd6f4"
)
title_label.pack(pady=(28, 4))

subtitle_label = tk.Label(
    window,
    text="Choose your move and beat the computer!",
    font=("Segoe UI", 10),
    bg="#1e1e2e",
    fg="#6c7086"
)
subtitle_label.pack(pady=(0, 18))

# ---- Score Card ----
score_card = tk.Frame(window, bg="#181825", pady=10)
score_card.pack(fill="x", padx=35)

score_label = tk.Label(
    score_card,
    text="You: 0     Ties: 0     Computer: 0",
    font=("Segoe UI", 12, "bold"),
    bg="#181825",
    fg="#89b4fa"    # blue
)
score_label.pack()

# ---- Result Card (shows choices + winner) ----
result_card = tk.Frame(window, bg="#2a2a3e", pady=15)
result_card.pack(fill="x", padx=35, pady=14)

# Player and Computer choices sit side by side
choices_row = tk.Frame(result_card, bg="#2a2a3e")
choices_row.pack()

# Player choice box
player_box = tk.Frame(choices_row, bg="#313145", width=130, height=100)
player_box.pack(side="left", padx=12, pady=5, ipadx=10, ipady=8)
player_box.pack_propagate(False)

player_top = tk.Label(
    player_box,
    text="YOU",
    font=("Segoe UI", 8, "bold"),
    bg="#313145",
    fg="#89b4fa"
)
player_top.pack(pady=(6, 0))

player_choice_label = tk.Label(
    player_box,
    text="❓\nYour Choice",
    font=("Segoe UI", 14),
    bg="#313145",
    fg="#cdd6f4",
    justify="center"
)
player_choice_label.pack(expand=True)

# VS label in the middle
vs_label = tk.Label(
    choices_row,
    text="VS",
    font=("Segoe UI", 16, "bold"),
    bg="#2a2a3e",
    fg="#585b70"
)
vs_label.pack(side="left", padx=10)

# Computer choice box
comp_box = tk.Frame(choices_row, bg="#313145", width=130, height=100)
comp_box.pack(side="left", padx=12, pady=5, ipadx=10, ipady=8)
comp_box.pack_propagate(False)

comp_top = tk.Label(
    comp_box,
    text="COMPUTER",
    font=("Segoe UI", 8, "bold"),
    bg="#313145",
    fg="#f38ba8"    # red/pink
)
comp_top.pack(pady=(6, 0))

computer_choice_label = tk.Label(
    comp_box,
    text="❓\nComputer",
    font=("Segoe UI", 14),
    bg="#313145",
    fg="#cdd6f4",
    justify="center"
)
computer_choice_label.pack(expand=True)

# ---- Result Message ----
result_label = tk.Label(
    result_card,
    text="Make your move!",
    font=("Segoe UI", 14, "bold"),
    bg="#2a2a3e",
    fg="#6c7086"
)
result_label.pack(pady=(14, 5))

# ---- Divider ----
tk.Frame(window, bg="#313145", height=1).pack(fill="x", padx=35, pady=2)

# ---- Buttons Section Label ----
choose_label = tk.Label(
    window,
    text="Choose Your Move",
    font=("Segoe UI", 11, "bold"),
    bg="#1e1e2e",
    fg="#cdd6f4"
)
choose_label.pack(pady=(16, 10))

# ---- Three Move Buttons ----
buttons_frame = tk.Frame(window, bg="#1e1e2e")
buttons_frame.pack(pady=4)

# Button styling — each button is a card with an emoji and label
button_data = [
    ("Rock",     "🪨", "#7c3aed", "#6d28d9"),   # purple
    ("Paper",    "📄", "#0369a1", "#075985"),    # blue
    ("Scissors", "✂️",  "#b45309", "#92400e"),   # amber
]

for choice, emoji, color, hover_color in button_data:
    btn_frame = tk.Frame(buttons_frame, bg=color, cursor="hand2")
    btn_frame.pack(side="left", padx=8, ipadx=4, ipady=4)

    emoji_lbl = tk.Label(
        btn_frame,
        text=emoji,
        font=("Segoe UI", 30),
        bg=color,
        fg="white",
        cursor="hand2"
    )
    emoji_lbl.pack(padx=18, pady=(12, 2))

    text_lbl = tk.Label(
        btn_frame,
        text=choice,
        font=("Segoe UI", 11, "bold"),
        bg=color,
        fg="white",
        cursor="hand2"
    )
    text_lbl.pack(pady=(2, 12))

    # Make the whole card clickable (not just the button widget)
    for widget in [btn_frame, emoji_lbl, text_lbl]:
        widget.bind("<Button-1>", lambda e, c=choice: play(c))

        # Hover effects — darken on hover
        widget.bind("<Enter>", lambda e, f=btn_frame, h=hover_color: f.config(bg=h) or
                    [w.config(bg=h) for w in f.winfo_children()])
        widget.bind("<Leave>", lambda e, f=btn_frame, n=color: f.config(bg=n) or
                    [w.config(bg=n) for w in f.winfo_children()])

# ---- How to Play Section ----
rules_card = tk.Frame(window, bg="#181825")
rules_card.pack(fill="x", padx=35, pady=18)

rules_title = tk.Label(
    rules_card,
    text="How to Play",
    font=("Segoe UI", 9, "bold"),
    bg="#181825",
    fg="#585b70"
)
rules_title.pack(pady=(8, 2))

rules_text = tk.Label(
    rules_card,
    text="🪨 Rock beats Scissors   •   📄 Paper beats Rock   •   ✂️ Scissors beats Paper",
    font=("Segoe UI", 9),
    bg="#181825",
    fg="#45475a"
)
rules_text.pack(pady=(0, 6))

# ---- Reset Button ----
reset_btn = tk.Button(
    window,
    text="🔄  Reset Game",
    font=("Segoe UI", 10, "bold"),
    bg="#313145",
    fg="#cdd6f4",
    activebackground="#45475a",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2",
    command=reset_game
)
reset_btn.pack(pady=(0, 6), ipadx=16, ipady=6)

# ---- Footer ----
tk.Label(
    window,
    text="Made with ❤️ using Python & Tkinter",
    font=("Segoe UI", 9),
    bg="#1e1e2e",
    fg="#313145"
).pack(pady=(4, 14))

# ---- Start the app ----
window.mainloop()