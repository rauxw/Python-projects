alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter  # Keep spaces, punctuation, etc.
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    deciphered_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
            deciphered_text += alphabet[shifted_position]
        else:
            deciphered_text += letter
    print(f"Here is the decoded result: {deciphered_text}")

def main():
    while True:
        decode = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift %= 26  # Normalize large shift values

        if decode == "encode":
            encrypt(original_text=text, shift_amount=shift)
        elif decode == "decode":
            decrypt(original_text=text, shift_amount=shift)
        else:
            print("Invalid option. Please type 'encode' or 'decode'.")

        re_run = input("Do you want to go again? (yes or no):\n").lower()
        if re_run != "yes":
            print("Goodbye!")
            break

main()
