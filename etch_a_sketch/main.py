# Etch a sketch game
import time
import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.title("Etch a Sketch!!!")
screen.listen()


def clear_Screen():
    # screen.clear()
    # screen.reset()
    # print(turtle.turtles())
    tim.clear()
    tim.reset()
    # screen.resetscreen()


def forward_mov():
    tim.forward(10)


def backward_mov():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def exit():
    screen.bye()


screen.onkey(fun=clear_Screen, key="C")  # this is a higher order method because it takes in a function as an argument
screen.onkeypress(fun=forward_mov, key="Up")
screen.onkeypress(fun=backward_mov, key="Down")
screen.onkeypress(fun=counter_clockwise, key="Left")
screen.onkeypress(fun=clockwise, key="Right")
# screen.exitonclick()
screen.onkey(fun=exit, key="X")
# while True:
#     print("hi")
#     screen.mainloop()

screen.mainloop()


# print("hi")
# does THE MAINLOOP EXIST ON ITS OWN?
#  THE DIFFERENCE BETWEEN SCREEN.CLEAR AND TIM.CLEAR()
