import colorgram
import colorgram

# Extract 6 colors
# colors = colorgram.extract('image.jpeg.jpeg', 25)
# rgb_clrs = []
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     new_color = (r, g, b)
#     rgb_clrs.append(new_color)
# print(rgb_clrs)

rgb_colors = [ (198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (109, 67, 85), (39, 35, 34), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48), (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181), (210, 200, 108), (178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59)]

#Chat gpt solution
import turtle as t
import random

# Setup screen
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Choose color list (from above)
color_list = rgb_colors

# Dot painting settings
dots_per_row = 10
dot_count = 100
dot_size = 20
spacing = 50

# Move turtle to starting point
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# Draw dots
for dot in range(1, dot_count + 1):
    tim.dot(dot_size, random.choice(color_list))
    tim.forward(spacing)

    if dot % dots_per_row == 0:
        tim.setheading(90)
        tim.forward(spacing)
        tim.setheading(180)
        tim.forward(spacing * dots_per_row)
        tim.setheading(0)

# Exit on click
screen = t.Screen()
screen.exitonclick()