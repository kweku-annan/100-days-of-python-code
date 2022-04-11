"""
INSTRUCTIONS
Prime numbers are numbers that can only be divided clearly by itself and 1.

You need to write a function that checks whether if the number passed into it is a prime number or not.
"""


def prime_checker(number):
    if number > 1 and number != 2:
        is_prime = True
        for i in range(2, number):
            # print(i)
            if number % i == 0:
                is_prime = False
        if is_prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
    elif number == 2:
        print("It's a prime number")
        # print(number)
    else:
        print("It's not a prime number")


checking = True

while checking:
    n = int(input("Check this number: "))
    prime_checker(number=n)
