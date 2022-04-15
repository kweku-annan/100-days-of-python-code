from art import logo
import os


def clearConsole():
    command = "cls"
    if os.name == "posix":
        command = "clear"
    os.system(command)


print(logo)
print("Welcome to the secret auction program.")
bidders = {}


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for key in bidders:
        if bidders[key] > highest_bid:
            highest_bid = bidders[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}")


more_bidders = True

while more_bidders:
    name = input("What is your name?\n").lower()
    bid = int(input("What's your bid?\n$"))
    bidders[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()

    if other_bidders == "no":
        highest_bidder(bidders)
        more_bidders = False
    else:
        clearConsole()
