
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.canvas = Canvas(width=300,height = 250)
        self.canvas.grid(column = 0,row = 1,columnspan = 2,pady = 50)
        self.q_text = self.canvas.create_text(150,125,
                                              width= 280,
                                              text="text goes here",
                                              font=("Arial",20,"italic"),
                                              fill=THEME_COLOR)

        self.window.config(padx=20,pady=20,bg=THEME_COLOR,height=400,width=320)

        # buttons
        tick_image = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=tick_image,pady=20,padx=20,command=self.tick_check_answer)
        self.tick_button.grid(column = 0,row = 2)

        false_image = PhotoImage(file="images/false.png")

        self.wrong_button = Button(image=false_image,pady=20,padx=20,command=self.false_check_answer)
        self.wrong_button.grid(column = 1,row = 2)

        # label

        self.score_label = Label(text=f"Score :{self.quiz.score}",highlightthickness=0,bg=THEME_COLOR,fg="white")
        self.score_label.grid(column = 1 ,row = 0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text_1 = self.quiz.next_question()

            self.canvas.itemconfig(self.q_text,text = q_text_1)
        else:
            self.canvas.itemconfig(self.q_text,text = f"You have completed the quiz!\n"
                                                      f"Final score is {self.quiz.score}")
            self.tick_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def tick_check_answer(self):
        tick = "true"
        is_right = self.quiz.check_answer(tick)
        self.give_feedback(is_right)
        self.get_next_question()

    def false_check_answer(self):
        wrong = "false"
        is_right = self.quiz.check_answer(wrong)
        self.give_feedback(is_right)
        self.get_next_question()

    def give_feedback(self,user_input):
        if user_input :
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.canvas_bg)

    def canvas_bg(self):
        self.canvas.config(bg="white")
        self.score_label.config(text = f"Score :{self.quiz.score}")