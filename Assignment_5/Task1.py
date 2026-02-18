students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Eve": 76
}
student_name = input("Enter student's name: ")

if student_name not in students :
    print("Student not found")
else :
    print(f"{student_name}'s marks: {students[student_name]}")