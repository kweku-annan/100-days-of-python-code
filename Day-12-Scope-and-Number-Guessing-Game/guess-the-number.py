import random

print("Welcome to the Number Guessing Game!")
difficulty = input("Choose a difficulty. Type 'easy' or hard: ").lower()
if difficulty == 'easy':
    lives = 10
else:
    lives = 5

print(f"You have {lives} attempts remaining to guess the number.")
chosen_number = random.randint(0, 100)

while lives > 0:
    guess_number = int(input("Make a guess: "))
    if guess_number > chosen_number:
        print(f"{guess_number} is too high.\nGuess again.")
        lives -= 1
        print(f"You have {lives} remaining to guess the number.")
    elif guess_number < chosen_number:
        print(f"{guess_number} is too low.\nGuess again.")
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
    else:
        print(f"You got it. The answer was {chosen_number}")
        print(f"You have {lives} attempts remaining to guess the number.")
        break


