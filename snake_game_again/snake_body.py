from turtle import Turtle, Screen, tracer, update
import random, time


class Snake:
    def __init__(self, location, snake_colour, snake_moveDistance):
        self.color = "white"
        self.shape = "square"
        self.snakeObjectList = []
        self.snake_MoveDistance = snake_moveDistance
        self.intro(position=location, s_color=snake_colour)

    def intro(self, position, s_color):
        for _ in range(3):
            tim = Turtle(shape=self.shape)
            tim.penup()
            tim.color(s_color[_])
            if self.snakeObjectList:
                tim.setpos(self.snakeObjectList[-1].xcor() - 20, self.snakeObjectList[-1].ycor())
            else:
                tim.setpos(position)
            self.snakeObjectList.append(tim)

    def snakeSizeIncrease(self):
        snake_body = Turtle(shape=self.shape)
        snake_body.color("white")
        snake_body.penup()
        if self.snakeObjectList:
            snake_body.setpos(self.snakeObjectList[-1].xcor() - 20, self.snakeObjectList[-1].ycor())
        self.snakeObjectList.append(snake_body)

    def snake_move(self):
        for index in range(len(self.snakeObjectList) - 1, 0, -1):
            self.snakeObjectList[index].setpos(self.snakeObjectList[index - 1].pos())
            # time.sleep(2)
        self.snakeObjectList[0].forward(20)

        time.sleep(0.05)

    def key_right(self):
        if self.snakeObjectList[0].heading() == 90:
            self.snakeObjectList[0].right(90)
        elif self.snakeObjectList[0].heading() == 270:
            self.snakeObjectList[0].left(90)

    def key_left(self):
        if self.snakeObjectList[0].heading() == 90:
            self.snakeObjectList[0].left(90)
        elif self.snakeObjectList[0].heading() == 270:
            self.snakeObjectList[0].right(90)

    def key_up(self):
        if self.snakeObjectList[0].heading() == 0:
            self.snakeObjectList[0].left(90)
        elif self.snakeObjectList[0].heading() == 180:
            self.snakeObjectList[0].right(90)

    def key_down(self):
        if self.snakeObjectList[0].heading() == 0:
            self.snakeObjectList[0].right(90)
        elif self.snakeObjectList[0].heading() == 180:
            self.snakeObjectList[0].left(90)

    def snakeBodyCollision(self):
        for objects in self.snakeObjectList[1:]:
            snake_headXcor = self.snakeObjectList[0].pos()[0]
            snake_headYcor = self.snakeObjectList[0].pos()[1]
            body_xcor = objects.pos()[0]
            body_ycor = objects.pos()[1]
            body_x_collision = body_xcor-10 < snake_headXcor < body_xcor + 10
            body_y_collision = body_ycor - 10 < snake_headYcor < body_ycor + 10
            if body_x_collision and body_y_collision:
                return True
        return False

    # @property
    def snakeWallCollision(self):
        xcor = self.snakeObjectList[0].pos()[0]
        ycor = self.snakeObjectList[0].pos()[1]
        return xcor > 290 or xcor < -290 or ycor > 290 or ycor < -290

