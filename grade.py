
grades = {
    "std1": 90,
    "std2": 85,
    "std3": 95
}

# Ask user for a student name
student = input("Enter student name: ")

if student in grades:
    print(student, "has a grade of", grades[student])
else:
    print("Student not found.")