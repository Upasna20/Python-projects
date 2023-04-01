# TODO 1: Creating the paddle graphic and the ball along with the obstructions ands divider.
# TODO 2: Giving movement to the ball, thinking about its bouncing dynamics.
# TODO 3: Ball hitting the paddle.
# TODO 4: Ball hitting the obstructions.
# TODO 5: Ball hitting the floor and ceiling to bounce back.
# TODO 6: Creating the scoring system.
# TODO 7: Letting the ball appear after it misses one of the paddle.
# TODO 8: Letting it end automatically when player difference is greater than 5 points.
import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.tracer(0)
screen.listen()
screen.title('The Famous Pong Game')
screen.setup(width=800, height=600)
screen.bgcolor('black')
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen.onkey(key='Up', fun=r_paddle.Up)
screen.onkey(key='Down', fun=r_paddle.Down)
screen.onkey(key='W', fun=l_paddle.Up)
screen.onkey(key='S', fun=l_paddle.Down)


game_is_on = True
r_score = Score()
l_score = Score()

while game_is_on:
    screen.update()
    r_score.write(f"{ball.r_score} ", align='right', font=('Courier', 30, 'normal'))
    l_score.write(f"{ball.l_score} ", align='left', font=('Courier', 30, 'normal'))

    # while ball.xcor() < 320 and ball.ycor() < 250:
    ball.move()
    time.sleep(ball.ballspeed)
        # screen.update()
    # time.sleep(1)
    # ball.setheading(37)
    # while ball.xcor() < 320 and ball.ycor() < 250:
    #     ball.fd(10)
    #     screen.update()
    #     time.sleep(0.05)
    #     # ball.speed('slowest')
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        '''Earlier, I used a bounce function that would run on the go to function but I completely
        missed the fact that it would take place just once only at the one time when the if condition 
         is met and rest the ball afterwards would function on the move function than the bounce funciton 
         algorithm and that is pretty much why I could see a bounce but not the perfect collision types
         bounce.'''
    if abs(ball.xcor()-r_paddle.xcor()) < 28 and ball.ycor() in range(int(r_paddle.ycor()-50), int(r_paddle.ycor()+50)):
        ball.paddlebounce()
    if abs(ball.xcor()-l_paddle.xcor()) < 28 and ball.ycor() in range(int(l_paddle.ycor()-50), int(l_paddle.ycor()+50)):
        ball.paddlebounce()
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.reset()
        r_score.clear()
        l_score.clear()













screen.exitonclick()