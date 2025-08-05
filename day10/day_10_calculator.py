import os
import platform

def add(a,b):
  return a + b

def sub(a,b):
  return a - b

def mul(a,b):
  return a * b

def divide(a,b):
  return a / b

def resultOfOutput(value):
  return f"Result: {value}"

def calculator(first_number,choose_operation, second_number):
  if choose_operation == '+':
    result = add(first_number,second_number)
    return result
  elif choose_operation == '-':
    result = sub(first_number,second_number)
    return result
  elif choose_operation == '*':
    result = mul(first_number,second_number)
    return result
  elif choose_operation == '/':
    result = divide(first_number,second_number)
    return result

def main():

  is_function_running = True

  first_number = int(input("What's the first number?:"))

  while is_function_running:

    print("""
      +
      -
      *
      /
        """)
    choose_operation = input("Pick an operation:")
    second_number = int(input("What's the second number?:"))

    result = calculator(first_number,choose_operation,second_number)
    print(resultOfOutput(result))

    option = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation and to exit 'q': ").lower()

    if option == 'y':
      first_number = result
    elif option == 'n':
      if platform.system() == "windows":
        os.system("cls")
      else:
        os.system("clear")
      main()
    elif option == 'q':
      print("Goodbye!")
      is_function_running = False
    else:
      print(f"Invalid option ({option}) Exiting")
      is_function_running = False


main()