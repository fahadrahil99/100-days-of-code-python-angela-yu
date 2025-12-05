from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = ""
checks = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global  REPS
    global checks
    checks = ""
    REPS = 0

    window.after_cancel(timer)
    label1.config(text = "Timer")
    canvas.itemconfig(canvas_text,text="00:00")
    label2.config(text=checks)
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW)
window.config(padx=100,pady=50)
canvas = Canvas(width=200,height=224,highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image)
canvas_text = canvas.create_text(100,132,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.config(bg=YELLOW)
canvas.grid(column = 1,row = 1)

def count_down(count):
    global REPS
    global  checks
    global timer
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_text,text=f"{count_min}:{count_sec}")
    if count > 0 :
        timer = window.after(1000,count_down,count - 1)
    else:
        start_count()
        if REPS % 2 == 0:
            checks +=  "✓"
            label2.config(text = checks)



def start_count():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN *60
    long_break = LONG_BREAK_MIN * 60
    if REPS   == 8:
        count_down(long_break)
        label1.config(text="Break",fg = RED)
    elif REPS % 2 != 0:
        count_down(work_sec)
        label1.config(text="Work",fg = GREEN)
    else :
        count_down(break_sec)
        label1.config(text="Break",fg=PINK)

#label
label1 = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"bold"),bg=YELLOW)
label1.grid(column = 1,row = 0)

label2 = Label(fg=GREEN,font=(FONT_NAME,20,"bold"),bg = YELLOW)
label2.grid(row = 3,column = 1)
#buttons
button1 = Button(text="Start",command=start_count)
button1.grid(row=2,column = 0)

button2 = Button(text = "Reset",command=reset_timer)
button2.grid(row = 2,column = 2)



window.mainloop()