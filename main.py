from tkinter import *
import pandas
from random import *
BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    to_learn_data = pandas.read_csv("data/cards_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/cards.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = to_learn_data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_body, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = frame.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_body, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_know():
    to_learn.remove(current_card)
    final_data = pandas.DataFrame(to_learn)
    final_data.to_csv("data/cards_to_learn.csv", index=False)
    next_card()


frame = Tk()
frame.title("Flash Card")
frame.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

flip_timer = frame.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="image/card_front.png")
card_back_img = PhotoImage(file="image/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 70, "italic"))
card_body = canvas.create_text(400, 263, text="", font=("Ariel", 50, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="image/wrong.png")
wrong_button = Button(image=wrong_img,  borderwidth=0, highlightthickness=0, command=next_card).grid(row=1, column=0)

right_img = PhotoImage(file="image/right.png")
right_button = Button(image=right_img, borderwidth=0, highlightthickness=0, command=is_know).grid(row=1, column=1)

next_card()

frame.mainloop()
