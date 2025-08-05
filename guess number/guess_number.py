import random

def welcome():
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of number between 1 and 100")

def add_attempts():
  choice_difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
  if choice_difficulty == 'easy':
    return 10
  elif choice_difficulty == 'hard':
    return 5


def select_random_number():
  number = random.randint(1,100)
  return number

def main():

  welcome()

  attempts = add_attempts()

  random_number = select_random_number()

  while attempts > 0:

    print(f'You have {attempts} remaining to guess the number')

    guess = int(input("Make a guess: "))

    if guess > random_number:
      print("Too High")
    elif guess < random_number:
      print("Too Low")
    elif guess == random_number:
      print(f"You guessed it correct it is {random_number}")
      return

    attempts -= 1

  print(f"You ran out of attempts the number was {random_number}")

main()