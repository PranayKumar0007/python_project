from turtle import *
### Etch a sketch game
s= Screen()
#
# def move_forward():
#     t.forward(10)
# def move_back():
#     t.backward(10)
# def turn_left():
#     t.left(10)
# def turn_right():
#     t.right(10)
# def clear():
#     t.clear()
#     t.penup()
#     t.home()
#     t.pendown()

# s.listen()
# s.onkeypress(move_forward,"w")
# s.onkeypress(move_back,"s")
# s.onkeypress(turn_left,"a")
# s.onkeypress(turn_right,"d")
# s.onkeypress(clear,"c")

### Bet on the winning turtle game
import random
race_on = False
s.setup(600, 500)
user_input = s.textinput(title="Make your bet!",
                         prompt="""Which turtle will win the race?
Enter a colour from 'red,orange,yellow,blue,purple,green':""")
colors = ['red', 'orange', 'yellow', 'blue', 'purple', 'green']
y_coordinates = [-100, -50, 0, 50, 100,150]
all_turtles = []

if user_input:
    race_on = True

for turtle in range(0,6):
    new_t = Turtle("turtle")
    new_t.color(colors[turtle])
    new_t.penup()
    new_t.goto(-280, y_coordinates[turtle])
    all_turtles.append(new_t)


while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            race_on = False
            if turtle.pencolor() == user_input:
                print(f"YOU WIN!. The {turtle.pencolor()} turtle is the winner of the race!")
            else:
                print(f"You lose. The {turtle.pencolor()} turtle is the winner of the race!")
        rand_step = random.randint(5,20)
        turtle.forward(rand_step)



