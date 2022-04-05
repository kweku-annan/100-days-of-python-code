"""
INSTRUCTIONS
Prime numbers are numbers that can only be divided clearly by itself and 1.

You need to write a function that checks whether if the number passed into it is a prime number or not.
"""


def prime_checker(number):
    for i in range(2, number - 1):
        if number % i == 0:
            print(f"{number} is not a prime number")

        print(f"{number} is a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
