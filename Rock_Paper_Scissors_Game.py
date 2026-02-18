from tkinter import *
import random
from PIL import Image, ImageTk

# ------------------- Window Setup -------------------
root = Tk()
root.title("Rock Paper Scissors")
root.geometry("700x600")
root.configure(bg="#295054")  # Fixed background

# ------------------- Title -------------------
title_label = Label(
    root,
    text="🎮 Rock Paper Scissors 🎮",
    font="Arial 24 bold",
    bg="#295054",
    fg="#fff"
)
title_label.pack(pady=15)

# ------------------- Image -------------------
try:
    image = Image.open(
        "C:/Users/user/Documents/Rock Paper Scissors Game/jeux.png")
    image = image.resize((400, 300))  # Resize for window
    photo = ImageTk.PhotoImage(image)
    label_image = Label(root, image=photo, bg="#295054")
    label_image.pack(pady=20)
except:
    label_image = Label(
        root, text="[Image Not Found]", font="Arial 16", bg="#295054", fg="white")
    label_image.pack(pady=20)

# ------------------- Prompt -------------------
prompt_label = Label(
    root,
    text="Choose Your Move:",
    bg="#295054",
    font="Tahoma 20 bold",
    fg="#fff"
)
prompt_label.pack(pady=10)

# ------------------- Game Logic -------------------
options = ["Rock", "Paper", "Scissors"]
emoji_dict = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

# Variable for result
Result = StringVar()
Result.set("")


def play(user_choice=None):
    if not user_choice:
        Result.set("Please choose : Rock, Paper, or Scissors!")
        return

    comp_pick = random.choice(options)

    if user_choice == comp_pick:
        Result.set(
            f"🤝 Tie! {emoji_dict[user_choice]} vs {emoji_dict[comp_pick]}")
        result_entry.config(fg="#FF9800")  # Orange
    elif (user_choice == "Rock" and comp_pick == "Scissors") or \
         (user_choice == "Paper" and comp_pick == "Rock") or \
         (user_choice == "Scissors" and comp_pick == "Paper"):
        Result.set(
            f"🎉 You Win! {emoji_dict[user_choice]} beats {emoji_dict[comp_pick]}")
        result_entry.config(fg="#4CAF50")  # Green
    else:
        Result.set(
            f"💻 Computer Wins! {emoji_dict[comp_pick]} beats {emoji_dict[user_choice]}")
        result_entry.config(fg="#F44336")  # Red


def Reset():
    Result.set("")
    result_entry.config(fg="#000")  # Default black


def Exit():
    root.destroy()


# ------------------- Choice Buttons -------------------
button_frame = Frame(root, bg="#295054")
button_frame.pack(pady=20)


def create_choice_button(parent, text, bg_color, fg_color, cmd):
    return Button(parent, text=text, font="Tahoma 18 bold", bg=bg_color, fg=fg_color,
                  width=10, bd=0, relief=RIDGE, command=cmd)


rock_button = create_choice_button(
    button_frame, "Rock 🪨", "#FFC107", "#000", lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=15)

paper_button = create_choice_button(
    button_frame, "Paper 📄", "#03A9F4", "#fff", lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=15)

scissors_button = create_choice_button(
    button_frame, "    Scissors ✂️", "#8BC34A", "#fff", lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=15)

# ------------------- Result Entry -------------------
result_entry = Entry(root, textvariable=Result, font="Tahoma 20 bold", justify="center",
                     width=40, bd=3, relief=RIDGE, fg="#000")
result_entry.pack(pady=20)

# ------------------- Control Buttons -------------------
control_frame = Frame(root, bg="#295054")
control_frame.pack(pady=20)

play_button = Button(control_frame, text="PLAY", font="Tahoma 18 bold", bg="#4CAF50", fg="white", width=12,
                     command=lambda: play())
play_button.grid(row=0, column=0, padx=10)

reset_button = Button(control_frame, text="RESET", font="Tahoma 18 bold", bg="#2196F3", fg="white", width=12,
                      command=Reset)
reset_button.grid(row=0, column=1, padx=10)

exit_button = Button(control_frame, text="EXIT", font="Tahoma 18 bold", bg="#f44336", fg="white", width=12,
                     command=Exit)
exit_button.grid(row=0, column=2, padx=10)

# ------------------- Run Application -------------------
root.mainloop()
