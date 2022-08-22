from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.Level =1
        self.hideturtle()
        self.penup()
        self.goto(-270,270)
        self.update_scoreboard()

    #update the scoreboard each time
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.Level}", align="left", font=FONT)

    #to update the score evrytime
    def increase_level(self):
        self.Level +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="Center", font=FONT)