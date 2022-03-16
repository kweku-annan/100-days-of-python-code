"""
Adding Evens

INSTRUCTIONS
You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100.

Important, there should only be 1 print statement in your console ouput.
It should just print the final total and not every step of the calculation.

"""
one_hundred = range(2, 101, 2)
total = 0
for number in one_hundred:
    total += number
    # print(number)
print(total)
