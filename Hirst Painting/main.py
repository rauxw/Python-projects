import turtle as t
import random

t.colormode(255)

jack = t.Turtle()
jack.hideturtle()
jack.speed("fastest")
jack.penup()
color_list = [(248, 247, 240), (239, 250, 245), (251, 241, 247), (237, 243, 250), (235, 226, 87), (210, 161, 109), (113, 177, 212), (201, 5, 68), (230, 52, 128), (196, 77, 19), (217, 133, 177), (193, 164, 15), (34, 106, 166), (11, 21, 62), (32, 189, 114), (232, 224, 4), (18, 28, 171), (122, 188, 161), (204, 32, 127), (233, 165, 197), (14, 183, 211), (10, 45, 24), (38, 132, 72), (45, 15, 10), (105, 92, 210), (139, 219, 203), (185, 13, 6), (135, 218, 232), (229, 73, 45), (169, 180, 229)]

jack.setheading(225)
jack.forward(300)
jack.setheading(0)
number_of_dots = 100

for dot_counts in range(1, number_of_dots + 1):
  jack.dot(20,random.choice(color_list))
  jack.forward(50)

  if dot_counts % 10 == 0:
    jack.setheading(90)
    jack.forward(50)
    jack.setheading(180)
    jack.forward(500)
    jack.setheading(0)


screen = t.Screen()
screen.exitonclick()

