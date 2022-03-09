print("Welcome to the tip calculator.")
bill = input("What was the total bill?\n$")
people = input("How many people to split the bill?\n")
tip_percent = input("What percentage of tip would you like to give? 10, 12 or 15?\n")

tip = float(bill) * float(tip_percent)/100
total_bill = tip + float(bill)
individual_bill = total_bill / int(people)
print(f"Each person should pay: ${round(individual_bill, 1)}")