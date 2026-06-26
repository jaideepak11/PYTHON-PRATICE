def calculate_average(student_data):
    total = sum(student_data.values())
    return total / len(student_data)

def print_above_average(student_data, average):
    print("\nStudents scoring above average:")
    for name, mark in student_data.items():
        if mark > average:
            print(f"{name}: {mark}")

# Dictionary storing 10 students and their marks
students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 68,
    "Emma": 95,
    "Frank": 78,
    "Grace": 88,
    "Henry": 74,
    "Ivy": 92,
    "Jack": 80
}

# Calculate average mark
average_mark = calculate_average(students)

# Display average
print(f"Average Mark: {average_mark:.2f}")

# Print students above average
print_above_average(students, average_mark)
