"""
INSTRUCTIONS
Create a program using maths and f-strings that tells us how many days, weeks, and months we are left if we live until
90 years old.
It will take your current age as input and output a message with our time left in this format:
'You have x days, y weeks and z months left.

"""

age = input("What is your current age?\n")
wished_age = input("How many years do you wish to live?\n")
years_left = int(wished_age) - int(age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
