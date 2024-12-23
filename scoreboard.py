# scoreboard.py
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()
        return True  # Indicate that bricks should reset

    def game_won(self):
        self.goto(0, 0)
        self.write("YOU WON!", align="center", font=("Courier", 36, "bold"))
