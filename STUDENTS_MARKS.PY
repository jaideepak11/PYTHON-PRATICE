students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 78},
    {"name": "Charlie", "marks": 92},
    {"name": "David", "marks": 88},
    {"name": "Emma", "marks": 95},
    {"name": "Frank", "marks": 73},
    {"name": "Grace", "marks": 81},
    {"name": "Henry", "marks": 90},
    {"name": "Ivy", "marks": 87},
    {"name": "Jack", "marks": 79}
]

total = 0

for student in students:
    total += student["marks"]

average = total / len(students)

print("Average mark:", average)
print("\nStudents scoring above average:")

for student in students:
    if student["marks"] > average:
        print(student["name"], "-", student["marks"])
