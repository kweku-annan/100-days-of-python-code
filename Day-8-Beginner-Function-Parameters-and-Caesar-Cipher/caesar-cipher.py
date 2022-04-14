from art import logo

print(logo)


# TODO: Modify to include numbers

def caesar(text, shift_steps, encode_decode):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    final_text = ""
    if encode_decode == "decode":
        shift_steps *= -1
    for letter in text:
        if letter not in alphabet:
            final_text += letter
        else:
            letter_index = alphabet.index(letter)  # Get the current index of the letter.
            letter_index_shifted = letter_index + shift_steps  # Increase letter index by amount of shift
            alphabet_length = len(alphabet)
            if letter_index_shifted >= alphabet_length:
                letter_index_shifted %= alphabet_length
            new_letter = alphabet[letter_index_shifted]
            final_text += new_letter
    print(f"The {encode_decode}d of {text} is {final_text}")


game_continue = True
while game_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=message, shift_steps=shift, encode_decode=direction)

    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if go_again == "no":
        game_continue = False
