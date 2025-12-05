from tkinter import *
window = Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)

my_label = Label(text = "My Text",font=("Arial",20,"normal"))
my_label.grid(column = 0,row = 0)

Input = Entry()

Input.get()
Input.grid(column = 3,row = 2)

def button_click():
    my_label.config(text=Input.get())

button = Button(text="Click Here",command=button_click)
button.grid(column = 1,row = 1)

button2 = Button(text = "New Button")
button2.grid(column = 2,row = 0)



window.mainloop()