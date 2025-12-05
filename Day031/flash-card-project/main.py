import random
from tkinter import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
single_dict = {}
#
def flash():
    canvas.itemconfig(front_image,image = new_image)
    canvas.itemconfig(c_title,text="English",fill = "white")
    canvas.itemconfig(c_word,text = single_dict["English"],fill="white")

def french_word_generator(data_dict):
    global single_dict
    single_dict = random.choice(data_dict)
    f_word = single_dict["French"]
    canvas.itemconfig(front_image,image=my_image)
    canvas.itemconfig(c_title,text = "French",fill = "black")
    canvas.itemconfig(c_word,text = f_word,fill = "black" )

def random_fr_word():
    global fl
    window.after_cancel(fl)
    french_word_generator(data)
    fl = window.after(3000,flash)
def is_known():
    data.remove(single_dict)
    random_fr_word()
    new_data = pd.DataFrame(data)
    new_data.to_csv("data/words_to_learn.csv",index = False)
window = Tk()
window.title("Flashy")
window.config(height=726,width=1000,bg=BACKGROUND_COLOR)
window.config(pady=50,padx=50)
fl = window.after(3000,flash)
canvas = Canvas(width=800,height = 526)
my_image = PhotoImage(file = "images/card_front.png" )
front_image =canvas.create_image(400,263,image = my_image)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
c_title = canvas.create_text(400,150 ,text="French", font= ("Ariel",40,"italic"))
c_word = canvas.create_text(400,250,text ="word",font = ("Ariel",60,"bold") )
canvas.grid(row = 0 ,column =0 ,columnspan = 2)

try:
    dataframe = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    dataframe = pd.read_csv("data/french_words.csv")
    data = dataframe.to_dict(orient ="records")
else:
    data = dataframe.to_dict(orient = "records")

#Buttons
right_image = PhotoImage(file="images/right.png")
button1 = Button(image=right_image,highlightthickness=0,command=is_known)
button1.grid(row = 1,column = 1)
button1.config(padx= 50)
wrong_image = PhotoImage(file="images/wrong.png")
button2 = Button(image=wrong_image,highlightthickness=0,command=random_fr_word)
button2.grid(row =1 , column = 0)
button2.config(padx= 50)
new_image = PhotoImage(file="images/card_back.png")
random_fr_word()










window.mainloop()


