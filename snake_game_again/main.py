from turtle import Turtle, Screen, tracer, update
import random, time
from food import Food
from snake_body import Snake
from miscellaneous import text, Score

screen = Screen()
screen.tracer(0)
score = Score()
# TEXT = text()

screen.setup(width=600, height=600)
screen.bgcolor("black")
SNAKE_LOCATION = (0, 0)
SNAKE_COLOR = ("pink", "white", "blue")
SNAKE_MOVE_DISTANCE = 20  # should be greater than or equal to 20

snake = Snake(location=SNAKE_LOCATION, snake_colour=SNAKE_COLOR, snake_moveDistance=SNAKE_MOVE_DISTANCE)
screen.update()
screen.onkey(fun=snake.key_left, key="Left")
screen.onkey(fun=snake.key_right, key='Right')
screen.onkey(fun=snake.key_up, key='Up')
screen.onkey(fun=snake.key_down, key='Down')
screen.listen()

# snake_2 = snake_body.Snake()
# snake_2.intro((0, 80))
is_game_on = True
food = Food()

Welcome = text(goto=(0, 0))
Welcome.text_write(text="Welcome To The Snake Game!!!", Align="center", size=20)
screen.update()
time.sleep(1)
Welcome.clear()


def food_eaten():
    x = food.pos()[0]
    y = food.pos()[1]
    # print(snake.snakeObjectList[0].pos())
    xcor_check = x - 15 < snake.snakeObjectList[0].pos()[0] < x + 15
    ycor_check = y - 15 < snake.snakeObjectList[0].pos()[1] < y + 15
    return xcor_check and ycor_check


while is_game_on:
    snake.snake_move()
    screen.update()
    score.score_read()
    # if snake.snakeObjectList[0].pos() == (20.00, 0.00):
    #     print("hey")
    # print(type(food.pos()))
    if food_eaten():
        # print("hi")
        food.ht()
        food = Food()
        snake.snakeSizeIncrease()
        score.score_increase()

    # time.sleep(1)

    if snake.snakeBodyCollision() or snake.snakeWallCollision():
        is_game_on = False
        print("GAME OVER!!")
        score.game_ends()
        screen.update()
        time.sleep(1)

