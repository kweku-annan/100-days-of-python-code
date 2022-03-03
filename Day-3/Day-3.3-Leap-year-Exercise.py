"""
INSTRUCTIONS
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, with an extra
day in February.

This is how you work out if a particular year is a leap year:
On every year that is evenly divisible by 4 EXCEPT every year that is evenly divisible by 100 UNLESS
the year is also divisible by 400
"""
year = int(input("Which year do you want to check?\n"))

if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year")
