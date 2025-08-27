from turtle import *


class Paddle(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.color("white")
        self.penup()
        self.setx(x_cor)
        self.sety(y_cor)

    def move_up(self):
        if self.ycor() < 210:
            self.sety(self.ycor() + 30)

    def move_down(self):
        if self.ycor() > -210:
            self.sety(self.ycor() - 30)




