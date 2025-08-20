import pandas

words = pandas.read_csv("nato_phonetic_alphabet.csv")

words_format = {row.letter:row.code for (index, row) in words.iterrows()}

word = input("Enter a word:").upper()

output_list = [words_format[letter] for letter in word]

print(output_list)