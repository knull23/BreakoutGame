from turtle import Turtle

class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=1, stretch_len=3)

    def clear_brick(self):
        self.goto(1000, 1000)