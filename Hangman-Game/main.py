import random
from hangman_art import stages, logo
from hangman_words import word_list
from word_search import get_word_definition
import os


def clear_console():
    """This is a function to clear the console."""
    command = "clear"
    if os.name in ("nt", "dos"):  # If machine is running on Windows, use cls
        command = "cls"
    os.system(command)

# TODO:- Let the program display the meaning of the mystery word.


# Variables
word_list = word_list
chosen_word = random.choice(word_list)
display = []
lives = 6
guessed_word = []

# Create blanks
for letter in chosen_word:
    display.append("_")
print(display)

has_guessed_all = False
has_guessed = False

while not has_guessed_all:  # This loop will run as long as there is a "_" in display.
    if "_" in display:  # Check if "_" is found in display
        guess = input("Guess a letter: ").lower()  # If yes, then ask user to guess a letter.
        clear_console()
        if guess in guessed_word:
            print(f"You've already guessed the letter {guess}")
            print("".join(display))
        else:
            # Check guessed letter
            for i in range(len(chosen_word)):  # This loop will run according to the length of the word before it
                # will go
                # back to guess.
                if chosen_word[i] == guess:  # Checking if letter is same as the guessed letter.
                    display[i] = chosen_word[i]  # Replacing a "_" in display with guessed letter.
            if guess not in chosen_word:
                print(f"You guessed {guess}, That's not in the word. You lose a life.")
                lives -= 1
                print(stages[lives])
            if lives == 0:
                print(f"{''.join(display)}")
                print(f"The mystery word is {chosen_word}")
                print("You Lose!")
                has_guessed_all = True
                break
            print(f"{''.join(display)}")
            print(stages[lives])
            guessed_word.append(guess)
    else:
        has_guessed_all = True
        # print(f"{''.join(display)}")
        print("You win!!!")

# Get the definition of the chosen word.
print(get_word_definition(chosen_word))
