from tkinter import *

FONT = ("Arial", 15, "normal")

window = Tk()

window.title("Snake King")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="Welcome player", font=FONT)
my_label.grid(column=0, row=0)

# Button
def clicked():
  my_label.config(text=input_val.get())

button = Button(text="Button", command=clicked)
button.grid(column=2, row=1)

button_2 = Button(text="New Button", command=clicked)
button_2.grid(column=2, row=0)

# Entry
input_val = Entry(width=10)
input_val.grid(column=4, row=3)


window.mainloop()