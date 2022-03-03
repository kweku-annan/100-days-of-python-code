"""
INSTRUCTIONS
Write a program that calculates the Body Mass Index (BMI) based on user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
1. Under 18.5 they are underweight.
2. Over 18.5 but below 25 they have a normal weight
3. Over 25 but below 30 they are overweight
4. Over 30 but below 35 they are obese
5. Above 35 they are clinically obese
"""
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = float(weight) / float(height)**2
# print(f"Your BMI is {int(bmi)}")

if bmi <= 18.5:
    print(f"Your BMI is {round(bmi)}, you are underweight.")
elif 18.5 < bmi < 25:
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif 25 < bmi < 30:
    print(f"Your BMI is {round(bmi)}, you are overweight.")
elif 30 < bmi < 35:
    print(f"Your BMI is {round(bmi)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")
