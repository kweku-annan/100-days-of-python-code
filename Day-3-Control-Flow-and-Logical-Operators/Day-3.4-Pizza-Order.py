"""
INSTRUCTIONS.
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: +$1
"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L?\n").upper()
add_pepperoni = input("Do you want pepperoni? Y or N?\n").upper()
extra_cheese = input("Do you want cheese? Y or N?\n").upper()

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid Input")
# print(bill)

if size == "S" and add_pepperoni == "Y":
    bill += 2
elif size == "M" or size == "L" and add_pepperoni == "Y":
    bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")