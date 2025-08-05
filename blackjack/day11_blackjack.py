import random
import os
import platform

def deal_card():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(user_score, pc_score):
  if user_score == pc_score:
    return "Draw"
  elif pc_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif pc_score > 21:
    return "Opponent went over. You win"
  elif user_score > pc_score:
    return "You win"
  else:
    return "You lose"

def main():
  user_score = -1
  user_cards = []
  pc_score = -1
  pc_cards = []

  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    pc_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    pc_score = calculate_score(pc_cards)

    print(f"user card: {user_cards}, score: {user_score}")
    print(f"computer's first card: {pc_cards[0]}")

    if user_score == 0 or pc_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_choice = input("Type 'y' to add card and 'n' to pass:")
      if user_choice == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while pc_score != 0 and pc_score < 17:
    pc_cards.append(deal_card())
    pc_score = calculate_score(pc_cards)

  print(f"Your final hand : {user_cards} and score : {user_score}")
  print(f"Computer's final hand : {pc_cards} and score : {pc_score}")
  print(compare(user_score,pc_score))

main()

while True:
  main()
  restart_choice = input("Type 'y' to play again and 'n' to quit")

  if restart_choice == 'y':
    if platform.system() == 'windows':
      os.system("cls")
    else:
      os.system("clear")
    main()
  else:
    break
