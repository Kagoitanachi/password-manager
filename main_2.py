from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v",
               "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
               "R",
               "S", "T", "U", "V", "W", "X", "Y", "Z"]

    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    symbols = ["!", "@", "#", "$", "%", "^", "*"]

    num_letters = random.randint(4, 6)
    num_numbers = random.randint(4, 6)
    num_symbols = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(num_letters)]
    password_symbols = [random.choice(symbols) for _ in range(num_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(num_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# or we can do this instead

# password = ""
# for char in password_list:
#     password += char

    print(f"Your password is: {password}")


# definition to save


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Missing Values", message="Please be sure you have everything fill up.")

    is_it_done = messagebox.askokcancel(title=website, message=f"Those are the details you enter: \nEmail: {email}"
                                                               f" \nPassword: {password} \n Do you want to save it?")

    if is_it_done:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website}| {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
window.config(padx=50, pady=50)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "Your_Email@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# buttons

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)  # we give width to 36 so it will be bigger
add_button.grid(row=4, column=1, columnspan=2)  # we use column span so the button get size of 2 columns

window.mainloop()
