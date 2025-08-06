from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# print(timmy)

# timmy.shape("turtle")
# timmy.fillcolor("red")
# timmy.forward(100)

# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]

table.add_row(["Pikachu","Electric"])
table.add_row(["Squritle", "Water"])
table.add_row(["Charmander", "Fire"])

table.align = 'l'

print(table)