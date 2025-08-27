from turtle import Turtle, Screen
import time
import players_paddle
from score_board import Scoreboard
from moving_ball import *





s = Screen()
s.bgcolor("black")
s.title("The Pong Game")
s.setup(width=800, height=500)
s.tracer(0)

t = Turtle("arrow")
t.color("white")
t.pencolor("white")
t.speed("fastest")
t.hideturtle()
t.penup()
t.goto(0, 230)
t.setheading(270)


def draw_division():
    t.pendown()
    t.pensize(5)
    t.forward(12)
    t.penup()
    t.forward(12)
    t.pendown()
for i in range(19):
    draw_division()

scoreboard_1 = Scoreboard(40,180)
scoreboard_2 = Scoreboard(-40,180)
player1 = players_paddle.Paddle(360,0)
player2 = players_paddle.Paddle(-360,0)
### To move the paddles up or down
s.listen()
s.onkey(player1.move_up,"Up")
s.onkey(player1.move_down,"Down")
s.onkey(player2.move_up,"w")
s.onkey(player2.move_down,"s")
### The bouncing ball
ball = Ball()


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    s.update()



    ## to detect collision at the top and bottom
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_y()

    ## to detect collision with the paddle
    if ball.distance(player1) < 50 and ball.xcor() > 340 or ball.distance(player2) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    ### to detect when ball gets missed
    if ball.xcor() > 380:
        scoreboard_2.increase_score()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard_1.increase_score()
        ball.reset_position()


s.exitonclick()

















