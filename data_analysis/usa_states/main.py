import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States")
image_map = "blank_states_img.gif"
screen.addshape(image_map)
turtle.shape(image_map)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

  answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state's name?").title()

  if answer_state == "Exit":
    break
  if answer_state in all_states:
    if answer_state not in guessed_states:
       guessed_states.append(answer_state)
    else:
      pass
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(state_data.state.item())


states_not_guessed = []

for state in all_states:
  if state not in guessed_states:
    states_not_guessed.append(state)


output_file = pandas.DataFrame(states_not_guessed, columns=["Not guessed States"])

output_file.to_csv("missing_states.csv")