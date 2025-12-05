
from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import  pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    randint(8, 10)
    randint(2, 4)
    randint(2, 4)


    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letter_list + number_list + symbol_list

    shuffle(password_list)

    g_password ="".join(password_list)
    p_entry.insert(0,g_password)
    pyperclip.copy(g_password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = w_entry.get()
    username = us_entry.get()
    password = p_entry.get()
    new_data = {
        website : {
            "email": username,
            "password": password,
        }
    }
    if len(website) and len(password) != 0:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"The details entered are\nWebsite :{website}\n "
                                               f"Email : {username}\n Password :{password}\n")
        if is_ok:
            try:
                with open("save.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("save.json","w") as file:
                    json.dump(new_data,file,indent= 4)
            else:
                data.update(new_data)
                with open("save.json","w") as file:
                    json.dump(data,file,indent = 4)
            finally:

                w_entry.delete(0, END)
                p_entry.delete(0, END)
    else:
        messagebox.showinfo(title="oops", message="Please don't leave any fields empty")
    #-----------------------------Search Function---------------------------#

def search():
    website = w_entry.get()
    try :
        with open("save.json","r") as file:
            data = json.load(file)
    except FileNotFoundError :
        messagebox.showinfo(title = "Error", message= "No data file found")

    else :
        search_data = {}
        if website in data:
            search_data.update(data[website])
            messagebox.showinfo(title= "Password", message= f"Email = {search_data["email"]}\n"
                                                        f"Password = {search_data["password"]}")
        else:
            messagebox.showinfo(title="Error", message="No data for the given website!")


    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title( "Password Manager")
canvas = Canvas(width = 200,height= 200)
window.config(padx=50,pady=50)
image1 = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = image1)
canvas.grid(column = 1,row = 0)

#labels
label1 = Label(text="Website :")
label1.grid(row = 1 ,column = 0)

label2 = Label(text="Email/Username :")
label2.grid(row =2,column = 0)

label3 =Label(text="Password :")
label3.grid(row = 3 ,column = 0)
#Entries
w_entry = Entry(width=52)
w_entry.grid(row = 1 ,column = 1 ,columnspan = 2)
w_entry.focus()
us_entry = Entry(width=52)
us_entry.insert(0,"fahadrahil1999@gmial.com")
us_entry.grid(row = 2 ,column = 1,columnspan = 2)
p_entry = Entry(width = 34)
p_entry.grid(row =3 ,column = 1)

# buttons
button1 = Button(text="Add",width = 44,command=save)
button1.grid(row= 5,column = 1,columnspan = 2)

button2 = Button(text="Generate Password",width=14,command=password_generator)
button2.grid(row = 3,column = 2)

button3 = Button(text = "Search",width = 14,command=search)
button3.grid(row = 1 , column = 2)
window.mainloop()
