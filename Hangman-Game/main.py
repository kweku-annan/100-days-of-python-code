import random
from hangman_art import stages, logo
from hangman_words import word_list
import os


def clearConsole():
    """This is a function to clear the console."""
    command = "clear"
    if os.name in ("nt", "dos"):  # If machine is running on Windows, use cls
        command = "cls"
    os.system(command)


# TODO-1 - Update the word_list to use the 'word_list' from hangman_words.py
# TODO-2 - Import the logo from hangman_art.py and print it at the start of the game.
# TODO-3 - Import the stages from hangman_art.py
# TODO-4 - If the user has entered a letter they've already guessed, print the letter and let them know. Don' away a
#  life.
# TODO-6 - If the letter is not in the chosen word, print out the letter and let them know it is not in the chosen word
# Join all elements in the list and turn it  into a String.

print(logo)

# Variables
word_list = word_list
chosen_word = random.choice(word_list)
display = []
lives = 6
guessed_word = []

# Testing code
print(f"Psssst, the solution is {chosen_word}")

# Create blanks
for letter in chosen_word:
    display.append("_")
print(display)

has_guessed_all = False
has_guessed = False

while not has_guessed_all:  # This loop will run as long as there is a "_" in display.
    if "_" in display:  # Check if "_" is found in display
        guess = input("Guess a letter: ").lower()  # If yes, then ask user to guess a letter.
        clearConsole()
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
