import pandas

words = pandas.read_csv("nato_phonetic_alphabet.csv")

words_format = {row.letter:row.code for (index, row) in words.iterrows()}

def generate_phonetic():
  word = input("Enter a word:").upper()
  try:
    output_list = [words_format[letter] for letter in word]
  except KeyError:
    print("Only letters and alphabets allowed")
    generate_phonetic()
  else:
    print(output_list)

generate_phonetic()