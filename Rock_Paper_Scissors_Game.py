# ------------Import the necessary libraries-----:
from tkinter import *
import random
from PIL import Image, ImageTk

# ------------------- Window -------------------
window = Tk()
window.title("Rock Paper Scissors")
window.geometry("800x650")
window.configure(bg="#295054")

# ------------------- Title -------------------
title_label = Label(
    window,
    text="🎮 Rock Paper Scissors 🎮",
    font="Arial 24 bold",
    bg="#295054",
    fg="white"
)
title_label.pack(pady=10)

# ------------------- Image-------------------
try:
    image = Image.open(
        "C:/Users/user/Documents/Rock Paper Scissors Game/jeux.png")
    photo = ImageTk.PhotoImage(image)
    label_image = Label(window, image=photo, bg="#f0f0f0")
    label_image.pack(pady=10)
except:
    label_image = Label(
        window, text="[Image Not Found]", font="Arial 16", bg="#f0f0f0")
    label_image.pack(pady=10)

# ------------------- Choose User -------------------
Choose_user = Label(
    window,
    text="Choose Your Move:",
    bg="#295054",
    font="Tahoma 20 bold",
    fg="white"
)
Choose_user.pack(pady=10)

# ------------------- Result Labels -------------------
computer_label = Label(window, text="", font="Tahoma 20", bg="#295054")
computer_label.pack(pady=10)

result_label = Label(window, text="", font="Tahoma 24 bold", bg="#295054")
result_label.pack(pady=10)

# ------------------- Les Options -------------------
options = ["Rock", "Paper", "Scissors"]
emoji_dict = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}


def play(user_choice):
    comp_pick = random.choice(options)

    computer_label.config(
        text=f"Computer chose: {comp_pick} {emoji_dict[comp_pick]}", fg="white")

    # ----------------Determine winner---------------
    if user_choice == comp_pick:
        result_label.config(text=f"🤝 It's a Tie!", fg="#FF9800")
    elif (user_choice == "Rock" and comp_pick == "Scissors") or \
         (user_choice == "Paper" and comp_pick == "Rock") or \
         (user_choice == "Scissors" and comp_pick == "Paper"):
        result_label.config(
            text=f"🎉 You Win! {emoji_dict[user_choice]} beats {emoji_dict[comp_pick]}", fg="#4CAF50")
    else:
        result_label.config(
            text=f"💻 Computer Wins! {emoji_dict[comp_pick]} beats {emoji_dict[user_choice]}", fg="#F44336")


def Reset():
    computer_label.config(text="")
    result_label.config(text="")
    result_label.config(fg="#000")


def Exit():
    window.destroy()


# ------------------- Choice Buttons -------------------
button_frame = Frame(window, bg="#295054")
button_frame.pack(pady=20)


def create_button(parent, text, bg_color, fg_color, cmd):
    return Button(
        parent,
        text=text,
        font="Tahoma 18 bold",
        bg=bg_color,
        fg=fg_color,
        width=10,
        bd=0,
        relief=RIDGE,
        activebackground=bg_color,
        command=cmd
    )


rock_button = create_button(button_frame, " Rock 🪨",
                            "#FFC107", "#000", lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=15)

paper_button = create_button(
    button_frame, "Paper 📄", "#03A9F4", "#fff", lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=15)

scissors_button = create_button(
    button_frame, "   Scissors✂️ ", "#8BC34A", "#fff", lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=15)

# ------------------- Control Buttons -------------------
control_frame = Frame(window, bg="#295054")
control_frame.pack(pady=5)

reset_button = create_button(control_frame, "Reset", "#2196F3", "white", Reset)
reset_button.grid(row=0, column=0, padx=10)

exit_button = create_button(control_frame, "Exit", "#f44336", "white", Exit)
exit_button.grid(row=0, column=1, padx=10)


window.mainloop()
