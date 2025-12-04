from turtle import Turtle




class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0,275)
        self.update_scoreboard()
    def update_scoreboard(self):

        self.clear()
        self.write(f"Score : {self.score} High Score = {self.high_score}", False, "center", ("Arial", 15, "normal"))
    def high_score1(self):
        if self.score > self.high_score :
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f" GAME OVER ", False, "center", ("Arial", 20, "normal"))
    def scoreboard(self):

        self.score += 1
        self.update_scoreboard()


