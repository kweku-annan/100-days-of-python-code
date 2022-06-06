############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import os
import random


def deal_cards():
    """This function deals cards to both the user and the computer. That is, it randomly picks a number from a list of
    numbers and returns it."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(cards)
    return chosen_card


def sum_hands(hands):
    """This function takes a list as an input, loops through it and then returns the total of the elements of the
    list """
    total = 0
    for i in hands:
        total += i
    return total


def game_logic(user, computer):
    """This function implements the rules for this Blackjack game. It takes two lists and compares the sum of their
    elements. It then decides returns True or False based on the rules of the game. It also checks if the computers hand
    is less than 17"""
    while sum_hands(computer) < 17:  # dealing cards and checking if computer conforms to the rules of the game
        current_deal = deal_cards()
        # print(current_deal)
        if current_deal == 11 and sum_hands(computer) + current_deal > 21:
            current_deal = 1
        computer.append(current_deal)

    while sum_hands(user) < 21:
        # print(user)
        get_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        user_current_deal = deal_cards()
        # print(f"{user_current_deal=}")
        if get_card == 'y':
            if user_current_deal == 11 and sum_hands(user) + user_current_deal > 21:
                user_current_deal = 1
                user.append(user_current_deal)
                print(f"Your cards: {user_cards}, current score: {sum_hands(user)}")
                print(f"Computer's first card: {computer[0]}")
            else:
                user.append(user_current_deal)
                print(f"Your cards: {user_cards}, current score: {sum_hands(user)}")
                print(f"Computer's first card: {computer[0]}")
        elif get_card == 'n':
            break

    # Score rules
    if sum_hands(computer) < sum_hands(user) <= 21:  #
        print(f"Your final hand: {user}, final score: {sum_hands(user)}")
        print(f"Dealer's final hand: {computer}, final score: {sum_hands(computer)}")
        print("You win!")
    elif sum_hands(computer) > 21 and sum_hands(user) <= 21:
        print(f"Your final hand: {user}, final score: {sum_hands(user)}")
        print(f"Dealer's final hand: {computer}, final score: {sum_hands(computer)}")
        print(f"You win!\nDealer went over.")
    elif sum_hands(user) > 21 and sum_hands(computer) <= 21:
        print(f"Your final hand: {user}, final score: {sum_hands(user)}")
        print(f"Dealer's final hand: {computer}, final score: {sum_hands(computer)}")
        print("You went over!\nYou lose.")
    elif sum_hands(user) < sum_hands(computer) <= 21:
        print(f"Your final hand: {user}, final score: {sum_hands(user)}")
        print(f"Dealer's final hands: {computer}, final score: {sum_hands(computer)}")
        print("You lose!")
    elif sum_hands(user) == sum_hands(computer):
        print(f"Your final hands: {user}, final score: {sum_hands(user)}")
        print(f"Dealer's final hands: {computer}, final score: {sum_hands(computer)}")
        print("Draw")
    else:
        print(f"Your final hand: {user}, final score: {sum_hands(user)}")
        print(f"Dealer's final hands: {computer}, final score: {sum_hands(computer)}")


game_on = True

while game_on:
    user_cards = [deal_cards(), deal_cards()]
    computer_cards = [deal_cards(), deal_cards()]

    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    # game_logic(user_cards, computer_cards)
    if start_game == 'y':
        print(logo)
        print(f"Your cards: {user_cards}, current score: {sum_hands(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        game_logic(user_cards, computer_cards)
        os.system("clear")
    else:
        game_on = False
