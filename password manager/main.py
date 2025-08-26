from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json

def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols

    password = ''.join(random.choice(all_chars) for _ in range(length))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?"
        )
        if is_ok:
            try:
                with open('data.json', mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def find_password():
  website_name = website_entry.get()
  try:
    with open("data.json", "r") as data_file:
      data = json.load(data_file)
  except FileNotFoundError:
      messagebox.showinfo(title="Error", message="No Data File Found!")
  else:
    if website_name in data:
      password = data[website_name]["password"]
      password_entry.delete(0, END)
      password_entry.insert(0, password)
    else:
      messagebox.showinfo(title="Error", message=f"No details for '{website_name}' found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website Row
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

# Email/Username Row
email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, 'example@gmail.com')

# Password Row
password = Label(text="Password:")
password.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate", width=14, command=generate_password)
generate_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
