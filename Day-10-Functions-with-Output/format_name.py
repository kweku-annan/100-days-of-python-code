"""
Create a function that will take two inputs (First name and last name) in any format and then changes it to
a title case format as an output.
"""


def format_name(first_name, last_name):
    return f"{first_name.capitalize()} {last_name.capitalize()}"


given_name = input("Enter your first name: ")
surname = input("Enter your surname: ")

output = format_name(given_name, surname)
print(output)
