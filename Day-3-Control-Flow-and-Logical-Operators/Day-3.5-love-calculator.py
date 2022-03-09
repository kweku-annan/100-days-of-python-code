"""INSTRUCTIONS
You are going to write a program that tests the compatibility between two people. We're going to use
the super scientific method recommended by BuzzFeed.

To work out the love score between two people:
name2 = input("What is their name?\n")

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the
number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2-digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is x, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is y, you are alright together."

Otherwise, the message will just be their score.
"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combined_string = name1 + name2
combined_string_lower = combined_string.lower()

t = combined_string_lower.count("t")
r = combined_string_lower.count("r")
u = combined_string_lower.count("u")
e = combined_string_lower.count("e")

true = t + r + u + e

l = combined_string_lower.count('l')
o = combined_string_lower.count('o')
v = combined_string_lower.count('v')
e = combined_string_lower.count('e')

love = l + o + v + e

love_score = str(true) + str(love)

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go like coke and mentos")
elif 40 < int(love_score) < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
