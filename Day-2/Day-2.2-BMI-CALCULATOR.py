"""
INSTRUCTIONS
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is calculated by dividing a person's weight (in kg) by the square of the height.
"""
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = float(weight) / (float(height))**2
print(f"Your BMI is {int(bmi)}")