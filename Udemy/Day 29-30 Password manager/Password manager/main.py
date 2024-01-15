import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_entry.delete(0, END)
    password_list = []

    password_list += [random.choice(letters) for num in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for num in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for num in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SEARCH -------------------------------------- #
def search():

        try:
            with open(r"C:\Users\alazarix\Files\Day-29\data.json", mode="r") as data_file:
                data = json.load(data_file)
                
        except FileNotFoundError:
            messagebox.showinfo(title="BUGYBUGYBUG", message="FileNotFoundError ;D")

        else:
            if website_entry.get() in data:
                email = data[website_entry.get()]["email"]
                password = data[website_entry.get()]["password"]     
                messagebox.showinfo(title=f"Website: {website_entry.get()}", message=f"Username: {email}\nPassword: {password}")    
            else:
                messagebox.showinfo(title="ERROR!!!!", message="Website not Found")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    new_data = {
        website_entry.get(): {
            "email": user_name_entry.get(),
            "password": password_entry.get(),
        }
    }

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(user_name_entry.get()) == 0:
        messagebox.showinfo(title="Error", message="Missing field/s")
    
    else:
        is_good = messagebox.askokcancel(title="Password Manager", message="Is this info correct?")
        if is_good:

            try:
                with open(r"C:\Users\alazarix\Files\Day-29\data.json", mode="r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open(r"C:\Users\alazarix\Files\Day-29\data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4) 
            
            else:
                data.update(new_data)
                with open(r"C:\Users\alazarix\Files\Day-29\data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)


            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200, highlightthickness=0)
lock_image = PhotoImage(file=r"C:\Users\alazarix\Files\Day-29\logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")


user_name_label = Label(text="Email/Username:")
user_name_label.grid(row=2, column=0)

user_name_entry = Entry(width=50)
user_name_entry.grid(row=2, column=1, columnspan=2)
user_name_entry.insert(0, "aharonlazari@gmail.com")


password = Label(text="Password:")
password.grid(row=3, column=0)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)


generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add password", width=43, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2, sticky="w")





window.mainloop()