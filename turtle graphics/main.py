import turtle as t
import random

jack = t.Turtle()
t.colormode(255)
jack.speed("fastest")
jack.shape('turtle')

def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  color = (r, g, b)
  return color

def spirograph(num):
  for _ in range(num):
    jack.circle(100)
    jack.color(random_color())
    current_heading = jack.heading()
    jack.setheading(current_heading + 10)
    jack.circle(100)

spirograph(36)




screen = t.Screen()
screen.exitonclick()