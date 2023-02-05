# import colorgram
# color = colorgram.extract('image.jpg', 30)
# # print(color)
# Li = []
# # first_color = color[0]
# # print(first_color)
# # coloured = first_color.rgb.r
# # print(coloured)
# for i in color:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb = (r, g, b)
#     # print(rgb)
#     Li.append(rgb)
# print(Li)
# Li.remove((245, 243, 238))
# print(Li)
from turtle import Turtle, Screen
import random
color_list = [(246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
count = 0
screen = Screen()
screen.colormode(255)
screen.screensize(2000, 1500)
tim = Turtle()
tim.pu()
tim.speed('fastest')
tim.setheading(135)
tim.forward(350)
tim.setheading(0)
tim.hideturtle()
while count < 10:
    coord = tim.pos()
    # print(coord)
    for _ in range(10):
        C = random.choice(color_list)
        tim.color(C)
        tim.forward(50)
        tim.dot(20, C)
        # tim.width(width=20)
        # tim.forward(20)
    tim.setpos(coord[0], coord[1])
    # get the coordinates of the starting point
    tim.right(90)
    tim.forward(50)
    tim.left(90)
    count += 1
    # code to draw 1 line

screen.exitonclick()
    # get back to the start of the line via setx and set y feature.
    # move to the next line