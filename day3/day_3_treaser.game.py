print("Welcome to treasure Island !")
print("Your mission is to find treasure.")

road_choice = input("You are at cross road. Where you want to go? Type 'left' or 'right' ")

if road_choice == "left":
  option = input("You came to lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across ")
  if option == "swim":
    print("You got eat by Tina Shark")
    print("Game Over!")
  elif option == "wait":
    house_door_color = input("You arrived at island unharmed. There is a house with 3 doors red blue and green. Which color to choose?")
    if house_door_color == 'red':
      print("You got eat by Manga King")
      print("Game Over")
    elif house_door_color == "blue":
      print("Congrats you got Silver")
    elif house_door_color == "green":
      print("You are freed from this cursed land")
    else:
       print("Restart game and choose option")
  else:
     print("Restart game and choose option")
elif road_choice == 'right':
  option = input("You came across shoot the criminal place. There are three people here named: one, two and three, Choose who to save")
  if option == 'one':
    print("He ate you as he was a cannibal")
    print("Game over")
  elif option == 'two':
    print("You are saved and freed")
    print("Woo")
  elif option == 'three':
    print("You got sold to slavery")
    print("Game over")
  else:
    print("Restart game and choose option")
else:
   print("Restart game and choose option")