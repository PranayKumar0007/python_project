


from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x, y)  # Top center
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Courier", 50, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()