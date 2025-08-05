capitals = {
  "France":"Paris",
  "Germany":"Berlin",
  "UAE":"Dubai"
}

travel_log = {
  "France": ["Paris", "Little Gardens", "Flora King"],
  "Germany": ["Berlin", "Munchi", "Erasea"],
  "UAE": ["Dubai", "Abu Dabi", "Dubai Mall"]
}

# print(travel_log["France"][1])

nested_list = ["A","B",["C","D"]]

# print(nested_list[2][1])

travel_log = {
  "France": {
    "cities_visited" : ["Paris", "Lille", "Dijon"],
    "total_visited": 12
  },
   "Germany": {
    "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
    "total_visited": 5
  }
}

print(travel_log["Germany"]['cities_visited'][2])