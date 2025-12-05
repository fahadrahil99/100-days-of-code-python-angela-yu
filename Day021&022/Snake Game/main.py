import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")








is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        score.scoreboard()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.high_score1()
        snake.reset()



    for _ in snake.snakes_list[1:]:
        if snake.head.distance(_) < 10:
            score.high_score1()
            snake.reset()

















screen.exitonclick()
