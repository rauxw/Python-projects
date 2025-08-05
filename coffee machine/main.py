MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

resources = {
    "water": 1000,   # in milliliters
    "milk": 500,     # in milliliters
    "coffee": 200    # in grams
}

def resource_display_format():
  for keys, values in resources.items():
    print(f"{keys} : {values}")

def coffee_choice():
  choice = str(input("What would you like? (espresso/latte/cappuccino):")).lower()
  return choice

def insert_coins():
  coin_quarters = int(input("How many quarters?:")) * 0.25
  coin_dimes = int(input("How many dimes?:")) * 0.10
  coin_nickles = int(input("How many nickles?:")) * 0.05
  coin_pennies = int(input("How many pennies?:")) * 0.01

  total = coin_quarters + coin_dimes + coin_nickles + coin_pennies

  return total

def get_cost(coffee):
  return MENU[coffee]['cost']

def deduct_resources(coffee):
  ingredients = MENU[coffee]['ingredients']
  for item in ingredients:
    resources[item] -= ingredients[item]

def is_resource_sufficient(coffee):
  ingredients = MENU[coffee]['ingredients']
  for item, required in ingredients.items():
    if resources.get(item,0) < required:
      print(f"Sorry, not enough {item}.")
      return False
  return True

def process_order(coffee):
  if not is_resource_sufficient(coffee):
    return

  cost = MENU[coffee]['cost']
  coins = insert_coins()

  if coins >= cost:
    change = round(coins - cost, 2)
    deduct_resources(coffee)
    print(f"Here is your {coffee}. Enjoy!")
    if change > 0:
      print(f"Here is your change ${change}")
  else:
    print(f"Sorry, that's not enough money. Money refunded. You entered ${coins} but need ${cost}.")

def main():
  print("")
  print(" ---------- Coffee Machine Program ---------- ")
  print("")

  is_running = True

  while is_running:
    coffee_input = coffee_choice()

    if coffee_input == "report":
      resource_display_format()
    elif coffee_input == "off":
      print("Turning off Machine")
      is_running = False
    elif coffee_input in MENU:
      process_order(coffee_input)
    else:
      print("Invalid input. Please choose espresso, latte, cappuccino, report, or off.")

main()