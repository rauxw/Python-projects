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

def spirograph(size_of_graph):
  for _ in range(360 // size_of_graph):
    jack.color(random_color())
    jack.circle(100)
    current_heading = jack.heading()
    jack.setheading(current_heading + size_of_graph)

spirograph(1)



screen = t.Screen()
screen.exitonclick()