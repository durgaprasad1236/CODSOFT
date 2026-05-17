# ============================================
# Rock Paper Scissors Game
# Author: [Your Name]
# Date: May 2026
# Description: A GUI Rock Paper Scissors game
#              with score tracking and auto-
#              reset after each round result
# ============================================

import tkinter as tk
import random


# ---- All three possible choices ----
CHOICES = ["Rock", "Paper", "Scissors"]

# ---- Emoji for each choice ----
EMOJI = {
    "Rock":     "🪨",
    "Paper":    "📄",
    "Scissors": "✂️"
}

# ---- What each choice beats ----
BEATS = {
    "Rock":     "Scissors",
    "Paper":    "Rock",
    "Scissors": "Paper"
}

# ---- Score counters ----
player_score   = 0
computer_score = 0
tie_score      = 0

# ---- Flag to stop double-clicking during the 2s wait ----
round_in_progress = False


# ---- Computer picks randomly ----
def computer_pick():
    return random.choice(CHOICES)


# ---- Figure out who won the round ----
def get_result(player, computer):
    if player == computer:
        return "tie"
    elif BEATS[player] == computer:
        return "win"
    else:
        return "lose"


# ---- Reset just the round display (not scores) ----
def reset_round_display():
    global round_in_progress

    player_emoji_label.config(text="❓", fg="#6c7086")
    player_name_label.config(text="Your Choice", fg="#6c7086")

    computer_emoji_label.config(text="❓", fg="#6c7086")
    computer_name_label.config(text="Computer", fg="#6c7086")

    result_label.config(text="Make your move!", fg="#6c7086")
    result_card.config(bg="#2a2a3e")
    vs_label.config(fg="#45475a")

    # Allow the player to click again
    round_in_progress = False


# ---- Main game function — runs when player clicks a choice ----
def play(player_choice):
    global player_score, computer_score, tie_score, round_in_progress

    # Don't allow clicking while result is still showing
    if round_in_progress:
        return

    round_in_progress = True

    # Computer makes its pick
    comp_choice = computer_pick()

    # Work out who won
    result = get_result(player_choice, comp_choice)

    # Update scores and pick colors based on result
    if result == "win":
        player_score  += 1
        result_text    = "🎉  You Win!"
        result_color   = "#a6e3a1"   # green
        flash_bg       = "#1a3a2a"

    elif result == "lose":
        computer_score += 1
        result_text     = "💻  Computer Wins!"
        result_color    = "#f38ba8"  # red
        flash_bg        = "#3a1a1a"

    else:
        tie_score   += 1
        result_text  = "🤝  It's a Tie!"
        result_color = "#f9e2af"     # yellow
        flash_bg     = "#2e2a1a"

    # ---- Show player's choice ----
    player_emoji_label.config(text=EMOJI[player_choice], fg="white")
    player_name_label.config(text=player_choice, fg="#cdd6f4")

    # ---- Show computer's choice ----
    computer_emoji_label.config(text=EMOJI[comp_choice], fg="white")
    computer_name_label.config(text=comp_choice, fg="#cdd6f4")

    # ---- Show who won ----
    result_label.config(text=result_text, fg=result_color)
    result_card.config(bg=flash_bg)
    vs_label.config(fg=result_color)

    # ---- Update the score bar ----
    score_label.config(
        text=f"You  {player_score}  —  {tie_score}  —  {computer_score}  Computer"
    )

    # ---- After 2 seconds, clear the round display (but keep scores) ----
    window.after(2000, reset_round_display)


# ---- Full game reset — scores go back to zero ----
def reset_game():
    global player_score, computer_score, tie_score, round_in_progress

    # Cancel any pending auto-reset and allow fresh start
    round_in_progress = False

    player_score   = 0
    computer_score = 0
    tie_score      = 0

    score_label.config(text="You  0  —  0  —  0  Computer")
    reset_round_display()


# ============================================
#            BUTTON HOVER HELPERS
# ============================================

def on_hover(frame, labels, hover_color):
    frame.config(bg=hover_color)
    for lbl in labels:
        lbl.config(bg=hover_color)

def on_leave(frame, labels, normal_color):
    frame.config(bg=normal_color)
    for lbl in labels:
        lbl.config(bg=normal_color)


# ============================================
#              BUILD THE WINDOW
# ============================================

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("520x670")
window.resizable(False, False)
window.configure(bg="#1e1e2e")

# ---- Title ----
tk.Label(
    window,
    text="Rock  Paper  Scissors",
    font=("Segoe UI", 21, "bold"),
    bg="#1e1e2e",
    fg="#cdd6f4"
).pack(pady=(28, 3))

tk.Label(
    window,
    text="Pick your move — computer will respond!",
    font=("Segoe UI", 10),
    bg="#1e1e2e",
    fg="#6c7086"
).pack(pady=(0, 18))

# ---- Score Bar ----
score_bar = tk.Frame(window, bg="#181825", pady=10)
score_bar.pack(fill="x", padx=35)

score_label = tk.Label(
    score_bar,
    text="You  0  —  0  —  0  Computer",
    font=("Segoe UI", 12, "bold"),
    bg="#181825",
    fg="#89b4fa"
)
score_label.pack()

tk.Label(
    score_bar,
    text="Wins  —  Ties  —  Wins",
    font=("Segoe UI", 8),
    bg="#181825",
    fg="#45475a"
).pack(pady=(0, 4))

# ---- Result Card ----
result_card = tk.Frame(window, bg="#2a2a3e", pady=18)
result_card.pack(fill="x", padx=35, pady=14)

# Row that holds both choice boxes and the VS in the middle
choices_row = tk.Frame(result_card, bg="#2a2a3e")
choices_row.pack()

# -- Player choice box --
player_box = tk.Frame(choices_row, bg="#313145", width=140, height=110)
player_box.pack(side="left", padx=10)
player_box.pack_propagate(False)

tk.Label(
    player_box, text="YOU",
    font=("Segoe UI", 8, "bold"),
    bg="#313145", fg="#89b4fa"
).pack(pady=(8, 0))

player_emoji_label = tk.Label(
    player_box, text="❓",
    font=("Segoe UI", 26),
    bg="#313145", fg="#6c7086"
)
player_emoji_label.pack()

player_name_label = tk.Label(
    player_box, text="Your Choice",
    font=("Segoe UI", 10),
    bg="#313145", fg="#6c7086"
)
player_name_label.pack(pady=(0, 6))

# -- VS label in the middle --
vs_label = tk.Label(
    choices_row, text="VS",
    font=("Segoe UI", 15, "bold"),
    bg="#2a2a3e", fg="#45475a"
)
vs_label.pack(side="left", padx=12)

# -- Computer choice box --
comp_box = tk.Frame(choices_row, bg="#313145", width=140, height=110)
comp_box.pack(side="left", padx=10)
comp_box.pack_propagate(False)

tk.Label(
    comp_box, text="COMPUTER",
    font=("Segoe UI", 8, "bold"),
    bg="#313145", fg="#f38ba8"
).pack(pady=(8, 0))

computer_emoji_label = tk.Label(
    comp_box, text="❓",
    font=("Segoe UI", 26),
    bg="#313145", fg="#6c7086"
)
computer_emoji_label.pack()

computer_name_label = tk.Label(
    comp_box, text="Computer",
    font=("Segoe UI", 10),
    bg="#313145", fg="#6c7086"
)
computer_name_label.pack(pady=(0, 6))

# -- Result message --
result_label = tk.Label(
    result_card,
    text="Make your move!",
    font=("Segoe UI", 14, "bold"),
    bg="#2a2a3e",
    fg="#6c7086"
)
result_label.pack(pady=(14, 2))

# Small hint under result
tk.Label(
    result_card,
    text="Display resets automatically after 2 seconds",
    font=("Segoe UI", 8),
    bg="#2a2a3e",
    fg="#45475a"
).pack(pady=(0, 4))

# ---- Divider ----
tk.Frame(window, bg="#313145", height=1).pack(fill="x", padx=35, pady=(2, 14))

# ---- Choose Your Move label ----
tk.Label(
    window,
    text="Choose Your Move",
    font=("Segoe UI", 11, "bold"),
    bg="#1e1e2e",
    fg="#cdd6f4"
).pack(pady=(0, 10))

# ---- The Three Choice Buttons ----
buttons_frame = tk.Frame(window, bg="#1e1e2e")
buttons_frame.pack()

# Each entry: (label, emoji, normal color, hover color)
button_info = [
    ("Rock",     "🪨", "#5b21b6", "#4c1d95"),   # purple
    ("Paper",    "📄", "#075985", "#0c4a6e"),    # blue
    ("Scissors", "✂️",  "#92400e", "#78350f"),   # amber
]

for choice, emoji, normal_bg, hover_bg in button_info:

    card_frame = tk.Frame(buttons_frame, bg=normal_bg, cursor="hand2")
    card_frame.pack(side="left", padx=8, ipadx=6, ipady=6)

    emoji_lbl = tk.Label(
        card_frame, text=emoji,
        font=("Segoe UI", 32),
        bg=normal_bg, fg="white", cursor="hand2"
    )
    emoji_lbl.pack(padx=18, pady=(12, 2))

    name_lbl = tk.Label(
        card_frame, text=choice,
        font=("Segoe UI", 11, "bold"),
        bg=normal_bg, fg="white", cursor="hand2"
    )
    name_lbl.pack(pady=(2, 12))

    # Group all widgets so hover changes color on all of them together
    all_widgets = [emoji_lbl, name_lbl]

    for widget in [card_frame, emoji_lbl, name_lbl]:
        widget.bind("<Button-1>", lambda e, c=choice: play(c))
        widget.bind("<Enter>",    lambda e, f=card_frame, w=all_widgets, h=hover_bg:
                    on_hover(f, w, h))
        widget.bind("<Leave>",    lambda e, f=card_frame, w=all_widgets, n=normal_bg:
                    on_leave(f, w, n))

# ---- Rules reminder ----
rules_frame = tk.Frame(window, bg="#181825")
rules_frame.pack(fill="x", padx=35, pady=16)

tk.Label(
    rules_frame, text="How to Play",
    font=("Segoe UI", 9, "bold"),
    bg="#181825", fg="#585b70"
).pack(pady=(8, 2))

tk.Label(
    rules_frame,
    text="🪨 Rock beats Scissors   •   📄 Paper beats Rock   •   ✂️ Scissors beats Paper",
    font=("Segoe UI", 9),
    bg="#181825", fg="#45475a"
).pack(pady=(0, 8))

# ---- Reset Button ----
tk.Button(
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
).pack(ipadx=16, ipady=7)

# ---- Footer ----
tk.Label(
    window,
    text="Made with ❤️ using Python & Tkinter",
    font=("Segoe UI", 9),
    bg="#1e1e2e",
    fg="#313145"
).pack(pady=(10, 14))

# ---- Run the app ----
window.mainloop()
