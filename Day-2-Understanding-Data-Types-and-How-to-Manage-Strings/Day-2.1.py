"""
INSTRUCTIONS

Write a program that adds the digit in a two digit number. e.g. If the input was 35, then the output should be
3 + 5 = 8
"""

two_digit_number = input("Type a two digit number: ")
result = int(two_digit_number[0]) + int(two_digit_number[1])
print(result)