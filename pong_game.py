from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# screeen creation
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
# screen.delay(0)
screen.tracer(0)

l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()
    ball.speed(ball.move_speed)
    #collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()




    #collision with paddle

    if ball.distance(r_paddle) < 50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()


    if ball.xcor()>340:
        ball.go_back()
        scoreboard.l_point()

    if ball.xcor() < -340:
        ball.go_back()
        scoreboard.r_point()

    if scoreboard.r_score==10 or scoreboard.l_score==10:
        game_is_on=False




screen.exitonclick()
