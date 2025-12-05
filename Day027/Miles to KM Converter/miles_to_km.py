from tkinter import *


window = Tk()
window.title("Miles to KM Converter")
window.minsize(height=100,width=200)

#labels
data = 0
label1 = Label(text="Miles")
label1.config(padx=10,pady=10)
label1.grid(column = 2,row = 0)

label2 = Label(text="is equal to")
label2.config(padx=10,pady=10)
label2.grid(column = 0,row = 1)

label3 = Label(text=f"{data}")
label3.config(padx=10,pady = 10)
label3.grid(column = 1,row = 1)

label4 = Label(text = "Km")
label4.grid(column = 2 , row = 1)
label4.config(padx=10,pady=10)

#Entry

Input = Entry(window,justify="center",width=15)
Input.insert(END,string = f"0")

Input.grid(column = 1,row = 0)
def calculate():
    result = float(Input.get()) * 1.60934
    label3.config(text = f"{round(result,2)}" )

#button
button = Button(text="Calculate",command=calculate)
button.grid(column = 1 , row = 2)
button.config(padx=8,pady=8)


window.mainloop()


