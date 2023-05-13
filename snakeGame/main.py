from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

game_is_on = True

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
screen.listen()
snake = Snake()
screen.onkey(key='Up', fun=snake.Up)
screen.onkey(key='Down', fun=snake.Down)
screen.onkey(key='Right', fun=snake.Right)
screen.onkey(key='Left', fun=snake.Left)
food = Food()
scoreboard = Scoreboard()
snake.create_snake()
while game_is_on:
    # time.sleep(2)
    snake.move()
    screen.update()
    '''so either tweak the code in the move method in the snake class
    to bring a display quite like this or simply do it here as it is
    done. My concern was what if the screen.update function in the 
    snake object works here, well it does .'''
    time.sleep(0.1)
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        snake.new_part()
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        # game_is_on = False
        # scoreboard.gameover()
        snake.goto()
        scoreboard.check()
        snake.new_snake()

    for i in snake.segments[2:]:
        if snake.segments[0].distance(i) < 20:
            # game_is_on = False
            # scoreboard.gameover()
            snake.goto()
            scoreboard.check()
            screen.update()
            snake.new_snake()
            # scoreboard.update()
            # screen.update()

screen.exitonclick()
'''purana score continues and highscore
high score not updated until new food engulfed
the highscore updates only after the new food is taken in and then the new score doesn't reset to 0 rather continues 
from the last score
also the snake must disappear'''
