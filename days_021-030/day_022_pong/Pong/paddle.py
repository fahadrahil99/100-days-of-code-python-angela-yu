from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.teleport(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.resizemode("user")
        self.penup()
        self.speed("fastest")



    def up(self):
        pos = self.pos()
        self.teleport(pos[0],pos[1]+30)
    def down(self):
        pos = self.pos()
        self.teleport(pos[0],pos[1]-30)
