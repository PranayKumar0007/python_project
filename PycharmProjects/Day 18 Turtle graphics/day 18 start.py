from turtle import *
import turtle as t
timmy = Turtle()

timmy.shape("turtle")
timmy.color("LawnGreen")
# Challenge 1 to draw a square
        # for i in range(4):
        #     timmy.forward(100)
        #     timmy.right(90)

# Challenge 2 to draw a dotted line.Used chatgpt to browse and find the penup pendown attributes.
        # for i in range(20):
        #     timmy.forward(10)
        #     timmy.penup()
        #     timmy.forward(10)
        #     timmy.pendown()

#Challenge 3 to draw shapes with diff colours
# my solution
        # def triangle():
        #     for i in range(3):
        #         timmy.forward(100)
        #         timmy.right(120)
        # def square():
        #     timmy.color("red")
        #     for i in range(4):
        #         timmy.forward(100)
        #         timmy.right(90)
        # def pentagon():
        #     timmy.color("blue")
        #     for i in range(5):
        #         timmy.forward(100)
        #         timmy.right(72)
        # def hexagon():
        #     timmy.color("purple")
        #     for i in range(6):
        #         timmy.forward(100)
        #         timmy.right(60)
        # def heptagon():
        #     timmy.color("magenta")
        #     for i in range(7):
        #         timmy.forward(100)
        #         timmy.right(51.428)
        # def octagon():
        #     timmy.color("cyan")
        #     for i in range(8):
        #         timmy.forward(100)
        #         timmy.right(45)
        # def nonagon():
        #     timmy.color("orange")
        #     for i in range(9):
        #         timmy.forward(100)
        #         timmy.right(40)
        # def decagon():
        #     timmy.color("black")
        #     for i in range(10):
        #         timmy.forward(100)
        #         timmy.right(36)
        #
        # triangle()
        # square()
        # pentagon()
        # hexagon()
        # heptagon()
        # octagon()
        # nonagon()
        # decagon()
# Actual solution
    # import random
    # colors = ["red", "blue", "green", "yellow", "purple","black","orange","pink","brown","cyan"]
    # def draw_shape(num_sides):
    #     angle = 360 / num_sides
    #     for i in range(num_sides):
    #         timmy.forward(100)
    #         timmy.right(angle)
    # for shape_sides in range(3,11):
    #     timmy.color(random.choice(colors))
    #     draw_shape(shape_sides)

# t.colormode(255)
# import random
# directions = [0,90,180,270]
# timmy.speed("fastest")
# for i in range(200):
#     timmy.pensize(10)
#     timmy.forward(30)
#     timmy.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     timmy.setheading(random.choice(directions))

import turtle
# Used chat gpt to create my own drawing and did somw change.
# import turtle
#
# # Setup screen
# screen = turtle.Screen()
# screen.bgcolor("white")
#
# # Create turtle
# pen = turtle.Turtle()
# pen.shape("turtle")
# pen.color("black")
# pen.pensize(3)
# pen.speed(3)
#
# # Draw red heart outline
# pen.penup()
# pen.goto(0, -100)
# pen.pendown()
# pen.color("red")
# pen.begin_fill()
#
# pen.left(140)
# pen.forward(180)
# pen.circle(-90, 200)
# pen.left(120)
# pen.circle(-90, 200)
# pen.forward(180)
#
# pen.end_fill()
#
# # Write "RITHIKA" in the center
# pen.penup()
# pen.goto(0, 30)
# pen.color("black")
# pen.write("RITHIKA", align="center", font=("Arial", 30, "bold"))
#
# # Hide turtle and keep window open
# pen.color("lightgreen")
# screen.mainloop()
#
#
#
#
#


# CHallenge 4 is to draw a spirograph using the turtle
import random
timmy.speed("fastest")
def random_color():
    r = random.randint(0, 1)
    g = random.randint(0, 1)
    b = random.randint(0, 1)
    color = (r, g, b)
    return color
### my solution for challenge 4
def spirograph():
    timmy.speed(10)
    for i in range(72):

        timmy.color("black")
        timmy.circle(100)
        timmy.penup()
        timmy.left(5)
        timmy.pendown()
###actual solution
def actual_spirograph(gap_size):
    for i in range(int(360/gap_size)):
        timmy.color("black")
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)


actual_spirograph(360)

screen = Screen()
screen.exitonclick()