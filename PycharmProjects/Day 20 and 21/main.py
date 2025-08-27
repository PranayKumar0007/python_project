



from snake import *
from food import Food
from scoreboard import Scoreboard
import time
s = Screen()
s.bgcolor("black")
s.title("Pranay's Snake Game")
s.screensize(500, 500)
s.tracer(0)

snake = Snake()
food = Food()
sb = Scoreboard()

### Kinda figured out this part but had a problem in actually doing it. Instead of
#   creating diff methods for each direction i tried to fit in all directions in one
#   attribute.
### To provide directions to snake
s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")

game_on = True

while game_on:
    s.update()
    time.sleep(0.1)
    snake.move_snake()
    # for food
    if snake.head.distance(food) < 15:
        food.refresh()
        sb.increase_score()
        snake.extend_snake()
    ### for collisions
    if snake.head.xcor() > 360  or snake.head.xcor() < -380:
        sb.reset()
        snake.reset()

    elif snake.head.ycor() > 320 or snake.head.ycor() < -310:
        sb.reset()
        snake.reset()

    ### for tail
    ### used an if statment b4 but now used the "slicing" technique to
    ### slice snake.sp[] list to account for all the snake parts except the head.
    for sps in snake.sp[1:-1]:
        if snake.head.distance(sps) < 15:
            sb.reset()
            snake.reset()






s.exitonclick()











