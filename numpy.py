import numpy as np

# Ask the user to enter the number of students and subjects
num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

# Create a NumPy array to store the marks of each student in each subject
marks_array = np.zeros((num_students, num_subjects), dtype=int)

# Ask the user to enter the marks for each student in each subject
for i in range(num_students):
    print(f"Enter marks for Student {i + 1}:")
    for j in range(num_subjects):
        marks_array[i, j] = int(input(f"Subject {j + 1}: "))

# Calculate the total marks for each student
total_marks = np.sum(marks_array, axis=1)

# Calculate the percentage for each student
percentage = (total_marks / (num_subjects * 100)) * 100

# Define the grading system
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"

# Display the result in a tabular format
print("\nStudent\tTotal Marks\tPercentage\tGrade")
for i in range(num_students):
    print(f"Student {i + 1}\t{total_marks[i]}\t\t{percentage[i]:.2f}%\t\t{calculate_grade(percentage[i])}")
