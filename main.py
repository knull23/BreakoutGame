# main.py
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick
import time

# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Breakout Game")
screen.tracer(0)

# Create Game Objects
paddle = Paddle((0, -250))
ball = Ball()
scoreboard = Scoreboard()

# Global Bricks List
bricks = []


# Function to Build the Brick Wall
def build_bricks():
    global bricks
    # Clear existing bricks
    for brick in bricks:
        brick.clear_brick()
    bricks.clear()

    # Rebuild bricks
    x_start = -350
    y_start = 200
    for row in range(5):
        for col in range(10):
            brick = Brick((x_start + (col * 75), y_start - (row * 30)))
            bricks.append(brick)


# Initialize Bricks
build_bricks()

# Paddle Controls
screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

# Game Loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Ball Collision with Top Wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # Ball Collision with Side Walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Ball Collision with Paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.bounce_y()

    # Ball Collision with Bricks
    for brick in bricks[:]:  # Use a copy of the list to avoid iteration errors
        if ball.distance(brick) < 35:
            ball.bounce_y()
            brick.clear_brick()
            bricks.remove(brick)
            scoreboard.point()
            break

    # Ball Misses the Paddle
    if ball.ycor() < -280:
        ball.reset_position()
        if scoreboard.reset_score():
            build_bricks()
        paddle.goto(0, -250)

    # Win Condition
    if len(bricks) == 0:
        game_is_on = False
        scoreboard.game_won()

screen.exitonclick()

