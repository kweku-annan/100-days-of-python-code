# TODO: Modify to include numbers

def caeser(start_message, shift_message, direction):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    end_message = ""
    for letter in start_message:
        if letter == " " or letter not in alphabet:
            end_message += letter
        else:
            letter_index = alphabet.index(letter)
            if direction == "decode":
                shift_message *= -1
            letter_index_shifted = letter_index + shift_message
            alphabet_length = len(26)
            if letter_index_shifted >= alphabet_length:
                letter_index_shifted %= alphabet_length
            new_letter = alphabet[letter_index_shifted]
            end_message += new_letter
    print(f"Here's the {direction}d result: {end_message}")


def encrypt(raw_message, shift_raw):
    """This function is responsible for encrypting a message from user input"""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    encoded_word = []
    for letter in raw_message:  # Loop through each letter in message
        if letter == " " or letter not in alphabet:
            encoded_word.append(letter)
        else:
            letter_index = alphabet.index(letter)  # Get the index of current letter under loop
            letter_index_shifted = letter_index + shift_raw  # Shift the letter by adding shift to the letter's index
            alphabet_length = len(alphabet)  # Find the length of the alphabet list
            while letter_index_shifted >= alphabet_length:
                letter_index_shifted -= alphabet_length
            encoded_letter = alphabet[letter_index_shifted]
            encoded_word.append(encoded_letter)
    return "".join(encoded_word)


def decrypt(encrypted_message, shift_encrypted):
    "This function is responsible for decrypting a message from a user input"
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    decoded_word = []
    for letter in encrypted_message:
        if letter == " " or letter not in alphabet:
            decoded_word.append(letter)
        else:
            letter_index = alphabet.index(letter)
            letter_index_shifted = letter_index - shift_encrypted
            # print(letter_index_shifted)
            alphabet_length = len(alphabet)
            while letter_index_shifted >= alphabet_length:
                letter_index_shifted += alphabet_length
                # print(letter_index_shifted)
            decoded_letter = alphabet[letter_index_shifted]
            decoded_word.append(decoded_letter)
    return "".join(decoded_word)


game_continue = True
while game_continue:
    encode_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if encode_decode == "encode":
        message = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encoded = encrypt(message, shift)
        print(f"Here's the encoded result: {encoded}")
    elif encode_decode == "decode":
        message = input("Type your message:\n").lower()
        shift = int(input("Type the shift number"))
        decoded = decrypt(message, shift)
        print(f"Here's the decoded result: {decoded}")
    else:
        print("Sorry, I didn't get that. Kindly check your input.")

    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if go_again == "no":
        game_continue = False

# message = input("message").lower()
# shift = int(input("shift: "))
# print(encrypt(message, shift))
