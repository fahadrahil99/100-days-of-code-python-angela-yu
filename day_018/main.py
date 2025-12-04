import random
import turtle
from turtle import *
turtle.colormode(255)
tim = Turtle()
color_list = [(236, 225, 81), (202, 5, 72), (197, 165, 9), (235, 50, 130), (207, 75, 11), (110, 179, 217), (221, 162, 100), (235, 224, 6), (30, 188, 108), (22, 106, 174), (13, 23, 65), (17, 28, 175), (214, 135, 176), (9, 186, 215), (205, 29, 143), (229, 167, 199), (124, 189, 161), (8, 49, 28), (36, 133, 73), (126, 219, 233), (66, 21, 6), (60, 11, 26), (112, 89, 211), (141, 217, 202), (190, 15, 5), (235, 64, 36)]
tim.penup()
tim.hideturtle()
def fd(no_dots):
    for _ in range (no_dots):
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)
def spot_painting(rows,columns):
    y_cor = -200
    for _ in range(rows):
        tim.setposition(-200,y_cor)
        fd(columns)
        y_cor+= 50
spot_painting(12,10)

screen = Screen()
screen.exitonclick()
