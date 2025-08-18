names = []


with open ("Names/invited_names.txt") as file:
  names = [line.strip() for line in file]


with open ("Letters/starting_letter.txt", mode="r") as file:
  letter = file.read()


for name in names:
  new_letter = letter.replace("[name]", name)

  with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as letter_file:
    letter_file.write(new_letter)


