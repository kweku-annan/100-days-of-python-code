import random
'''
INSTRUCTIONS
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important: the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

You need to generate a random number, either 0 or 1.
1 means Heads 
0 means Tails
'''
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
