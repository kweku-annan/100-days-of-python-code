"""
INSTRUCTIONS

You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.
"""
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, separated by a comma.\n")
names = namesAsCSV.split(", ")

random_number = random.randint(0, len(names) - 1)
random_name = names[random_number]
print(f"{random_name} is going to pay for the meal today!")
