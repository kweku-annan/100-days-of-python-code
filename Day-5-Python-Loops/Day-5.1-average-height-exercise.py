"""
Average Height

INSTRUCTIONS
You are going to write a program that calculates the average student height from a List of heights.
eg. student_heights = [100, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together and dividing by the total number of heights.

IMPORTANT: You should not use the sum() or len() functions in your answer. You should try to replicate their
functionality using what you have learnt.
"""

student_heights = input("Input a list of student heights separated by ',': ").split(", ")

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

heights_total = 0
students_total = 0

for height in student_heights:
    heights_total += height
    students_total += 1
average = round(heights_total/students_total)
print(average)
