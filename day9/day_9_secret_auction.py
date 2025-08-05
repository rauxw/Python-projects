import os
import platform

def clear_screen():
  if platform.system() == "windows":
    os.system("cls")
  else:
    os.system("clear")

def main():
  bid_dict = {}
  while True:
    name = str(input("What is your name?:"))
    bid = int(input("Enter your bid:"))
    bid_dict[name] = bid


    stop_or_continue = str(input("Want to stop type 'yes' or 'no:")).lower()
    clear_screen()

    if stop_or_continue == "yes":
      break

  highest_bidder =max(bid_dict, key=bid_dict.get)
  highest_bid = bid_dict[highest_bidder]

  print(f"Highest bidder is : {highest_bid}")

main()
