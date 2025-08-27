

#### found this code in chatgpt when I asked to explain about tracer()
#
# from turtle import *
# s = Screen()
# s.bgcolor("black")
# s.title("Tracer Demo")
# s.tracer(3)
# colors = ["red", "green", "blue"]
#
# for i in range(3):
#     t = Turtle("turtle")
#     t.color(colors[i])
#     t.penup()
#     t.goto(i * 50, 0)
#
# s.update()  # Needed for tracer(0) or higher n
# s.mainloop()


from turtle import *

COORDS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP= 90
DOWN= 270
LEFT= 180
RIGHT= 0
class Snake:
    def __init__(self):
        self.sp = []
        self.create_snake()
        self.s = Screen()
        self.head = self.sp[0]

    def screen(self):
        self.s = Screen()
        self.s.bgcolor("black")
        self.s.title("Pranay's Snake Game")
        self.s.screensize(500, 500)
        self.s.tracer(0)

    def create_snake(self):
         for coord in COORDS:
             self.add_tail(coord)
            ### sp --- snake part

    def add_tail(self, coord):
         new_sp = Turtle("square")
         new_sp.color("white")
         new_sp.penup()
         new_sp.goto(coord)
         self.sp.append(new_sp)

    def extend_snake(self):
        self.add_tail(self.sp[-1].position())

    def move_snake(self):
            #### !!!!Important part to revise and imagine properly!!!!
            for snake_part in range(len(self.sp)-1,0,-1):
                new_x = self.sp[snake_part-1].xcor()
                new_y = self.sp[snake_part-1].ycor()
                self.sp[snake_part].goto(new_x,new_y)
            self.sp[0].forward(MOVE_DISTANCE)

    def reset(self):
        for sps in self.sp:
            sps.goto(1000,1000)
        self.sp.clear()
        self.create_snake()
        self.head = self.sp[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
       if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


















