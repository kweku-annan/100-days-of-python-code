print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
cross_road = input('''You are at a cross road. Where do you want to go? Type "left" or "right".\n''').lower()
if cross_road == "left":
    lake = input('''You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. 
    Type "swim" to swim across.\n''').lower()
    if lake == "wait":
        doors = input('''You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and 
        one blue. Which colour do you choose?\n''').lower()
        if doors == "yellow":
            print("You've found the treasure!.\nYou win!")
        elif doors == 'red':
            print("You enter a room full of snakes. The snakes are gonna use you for practice.\nGame Over!!!")
        else:
            print("You enter a room full of beasts. Your flesh is gonna be used for feast.\nGame Over!!!")
    elif lake == "swim":
        print("The are crocodiles and alligators in the lake.It's sad what they are gonna do to you.\nGame Over!")
    else:
        print("Invalid input.\nGame Over")
elif cross_road == "right":
    print("You walked straight into a hungry lion's den. You can image what will happen.\nGame Over!")
else:
    print("Invalid input.\nGame Over!")

