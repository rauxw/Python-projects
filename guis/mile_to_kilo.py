from tkinter import *

window = Tk()
window.title("Mile to Kilo Converter")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

def miles_to_kms():
  miles = int(miles_entry.get())
  km = miles * 1.609
  output_label.config(text=km)

miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

label_Mile = Label(text="Miles", font=("Arial", 20, "normal"))
label_Mile.grid(column=2, row=0)

label_Mile = Label(text="is equal to", font=("Arial", 15, "normal"))
label_Mile.grid(column=0, row=2)

output_label = Label(text=0, font=("Arial", 15, "normal"))
output_label.grid(column=1, row=2)

label_Mile = Label(text="Km", font=("Arial", 15, "normal"))
label_Mile.grid(column=2, row=2)

button = Button(text="Calculate", command=miles_to_kms)
button.grid(column=1, row=3)


window.mainloop()