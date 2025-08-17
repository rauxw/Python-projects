from turtle import Screen
from player import Player
import time

screen = Screen()

screen.setup(height=600, width=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()

screen.listen()

screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()

screen.exitonclick()