from turtle import Turtle

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.segment = Turtle()
        self.position = [(0, 0), (20, 0), (40, 0)]
        self.segments()

    def segments(self):
        for x in position:
            self.segment.shape("square")
            self.segment.goto(x)
            self.segment.penup()






