from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.x_cor = 0
        self.snakes_list=[]
        self.create_snake()
        self.head = self.snakes_list[0]


    def create_snake(self):
        x_cor = 0
        for x in range(0, 3):
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.setx(float(x_cor))
            x_cor -= 20
            self.snakes_list.append(snake)
    def extend(self):
        add_pos = self.snakes_list[-1].position()
        addon = Turtle()
        addon.shape("square")
        addon.color("white")
        addon.penup()
        addon.setposition(add_pos)
        self.snakes_list.append(addon)

    def reset(self):
        for x in self.snakes_list:
            x.goto(1000,1000)
        self.snakes_list.clear()
        self.create_snake()
        self.head = self.snakes_list[0]

    def move(self):
         for x in range(len(self.snakes_list) - 1, 0, -1):
             new_x = self.snakes_list[x - 1].xcor()
             new_y = self.snakes_list[x - 1].ycor()
             self.snakes_list[x].goto(new_x, new_y)
         self.snakes_list[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

