from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password(length=12):
    # Define character sets
    letters = string.ascii_letters  # a-z + A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # special characters

    # Combine all characters
    all_chars = letters + digits + symbols

    # Generate random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
  website = website_entry.get()
  email = email_username_entry.get()
  password = password_entry.get()

  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
  else:
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

    if is_ok:
      with open('data.txt', mode="a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, 'example@gmail.com')

password = Label(text="Password:")
password.grid(column=0, row=3)

password_entry = Entry()
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(column=2, row=3, columnspan=2)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()