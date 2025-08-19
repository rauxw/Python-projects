import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250819.csv")

fur_colors = data["Primary Fur Color"]

data_colors = data["Primary Fur Color"]

colors = {"Gray": 0, "Cinnamon": 0, "Black": 0}

for color in data_colors:
  if color in colors:
    colors[color] += 1

print(colors.items())

output_file = pandas.DataFrame(list(colors.items()), columns=["Colors", "Count"])
output_file.to_csv("colors.csv")