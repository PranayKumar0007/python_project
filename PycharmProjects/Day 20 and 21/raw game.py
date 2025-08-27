from turtle import *
import time
s = Screen()
s.bgcolor("black")
s.title("Pranay's Snake Game")
s.screensize(500,500)
s.tracer(0)


snake = []


coords = [(0,0),(-20,0),(-40,0)]

for coord in coords:
    new_t = Turtle("square")
    new_t.color("white")
    new_t.penup()
    new_t.goto(coord)
    snake.append(new_t)

game_on = True
while game_on:
    s.update()
    time.sleep(0.1)
    #### !!!!Important part to revise and imagine properly!!!!
    for snake_part in range(len(snake)-1,0,-1):
        new_x = snake[snake_part-1].xcor()
        new_y = snake[snake_part-1].ycor()
        snake[snake_part].goto(new_x,new_y)
    snake[0].forward(20)

