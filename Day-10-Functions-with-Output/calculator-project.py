def calc_function(f_number, n_number, sign):
    if sign == "+":
        print(f"{f_number} {sign} {n_number} = {f_number + n_number}")
        return f_number + n_number
    elif sign == "-":
        print(f"{f_number} {sign} {n_number} = {f_number - n_number}")
        return f_number - n_number
    elif sign == "*":
        print(f"{f_number} {sign} {n_number} = {f_number * n_number}")
        return f_number * n_number
    elif sign == "/":
        print(f"{f_number} {sign} {n_number} = {f_number / n_number}")
        return f_number / n_number
    else:
        return "Invalid Operation"


def calculator():
    first_number = float(input("What's your first number?: "))
    print("+\n-\n*\n/")
    continue_calculation = True
    while continue_calculation:
        operation = input("Pick and operation: ")
        next_number = float(input("What's the next number?: "))
        result = calc_function(first_number, next_number, operation)

        new_calc = input(f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation: ").lower()
        if new_calc == 'y':
            first_number = result
        else:
            continue_calculation = False
            calculator()


calculator()
