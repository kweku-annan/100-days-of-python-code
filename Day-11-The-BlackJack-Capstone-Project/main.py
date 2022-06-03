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
    while sum_hands(computer) < 17:
        current_deal = deal_cards()
        print(current_deal)
        if current_deal == 11 and sum_hands(computer) + current_deal > 21:
            current_deal = 1
        computer.append(current_deal)

    if sum_hands(computer) < sum_hands(user) <= 21:
        return True
    elif sum_hands(user) < sum_hands(computer) <= 21:
        return False
    else:
        return "Draw"


while True:
    user_cards = [deal_cards(), deal_cards()]
    computer_cards = [deal_cards(), deal_cards()]

    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    game_logic(user_cards, computer_cards)
    if start_game == 'y':
        print(user_cards)
        print(computer_cards)
    else:
        pass
