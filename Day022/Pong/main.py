from turtle import Screen
import time
from paddle import Paddle
from ball import Ball

from pong.pythonProject1.scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")
screen.tracer(0)
R_POSITION = 350
L_POSITION = -350
paddle = Paddle(R_POSITION)
paddle2 = Paddle(L_POSITION)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.up,"Up")
screen.onkey(paddle.down,"Down")
screen.onkey(paddle2.up,"w")
screen.onkey(paddle2.down,"s")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle) < 50 and ball.xcor() > 330 or ball.distance(paddle2) < 50 and ball.xcor() < -330 :
        ball.bounce_x()

    if ball.xcor() > 370 :
        ball.reset_position()
        scoreboard.l_point()



    if  ball.xcor() < -370 :
        ball.reset_position()
        scoreboard.r_point()















screen.exitonclick()

