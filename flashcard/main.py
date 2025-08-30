from tkinter import *
import pandas
import random
import time
import os

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")

current_card = {}
to_learn = {}

try:
  data = pandas.read_csv('data/words_learned.csv')
except FileNotFoundError:
  original_data = pandas.read_csv('data/french_words.csv')
  to_learn = original_data.to_dict(orient="records")
else:
  to_learn = data.to_dict(orient="records")

def next_card():
  global current_card, flip_timer
  window.after_cancel(flip_timer)
  current_card = random.choice(to_learn)
  canvas.itemconfig(card_title, text="French")
  canvas.itemconfig(card_word, text=current_card["French"])
  canvas.itemconfig(card_background, image=card_front_img)
  flip_timer = window.after(3000, func=flip_card)

def flip_card():
  canvas.itemconfig(card_title, text="English")
  canvas.itemconfig(card_word, text=current_card["English"])
  canvas.itemconfig(card_background, image=card_back_img)

def is_known():
  to_learn.remove(current_card)
  print(len(to_learn))
  data = pandas.DataFrame(to_learn)
  data.to_csv('data/words_learned.csv', index=False)
  if len(to_learn) == 0:
    canvas.itemconfig(card_title, text="No words left")
    canvas.itemconfig(card_word, text="You learned all words")
  else:
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=FONT_TITLE)
card_word = canvas.create_text(400, 263, text="word", font=FONT_WORD)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image, border=0, command=next_card)
unknown_button.grid(column=0, row=1)

tick_image = PhotoImage(file='images/right.png')
known_button = Button(image=tick_image, border=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()



window.mainloop()


