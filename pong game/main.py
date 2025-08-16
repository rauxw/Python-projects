from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Ping Pong Ball")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))

ball = Ball()

score = Scoreboard()

screen.listen()

#right paddle controls
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

#left paddle controls
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  #Detect ball collision wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  #Detect collision with right paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
    ball.bounce_x()

  #Reset R paddle miss
  if ball.xcor() > 380:
    ball.reset_position()
    score.l_point()

  #Reset L paddle miss
  if ball.xcor() < -380:
    ball.reset_position()
    score.r_point()

screen.exitonclick()