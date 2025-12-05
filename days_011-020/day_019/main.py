import  random
from turtle import Turtle,Screen
screen = Screen()
screen.setup(width=500,height=400)
user_input = screen.textinput("Make Your Bet","Which turtle will win the race?.Enter the color  .")
colours = ["red","green","yellow","blue","black","purple"]
shape = "turtle"
position_y =[100,60,20,-20,-60,-100]
turtle_list = []
is_race_on = False
for x in range(0,6):
    turtle = Turtle(shape=shape)
    turtle.color(colours[x])
    turtle.penup()
    turtle.goto(-230, position_y[x])
    turtle_list.append(turtle)

if user_input:
    is_race_on = True
while is_race_on:
    for turtles in turtle_list:
        random_distance = random.randint(0, 10)
        turtles.forward(random_distance)
        if turtles.xcor() > 230:
            if user_input == turtles.pencolor():
                print(f"You've Won. The color of the turtle won is {turtles.pencolor()}.")
            else :
                print(f"You've lost. The color of the turtle won is {turtles.pencolor()}.")
            is_race_on = False

screen.exitonclick()