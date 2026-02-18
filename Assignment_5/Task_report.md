# Assignment 5 Report

## Task 1: Student Marks Dictionary

### Description
This program initializes a dictionary `students` containing student names as keys and their corresponding marks as values. It prompts the user to enter a student's name and prints their marks if found, or a "Student not found" message otherwise.

### Code
```python
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
```

### Output
```
Enter student's name: Alice
Alice's marks: 85

Enter student's name: Rushikesh
Student not found
```

## Task 2: List Slicing

### Description
This program demonstrates list slicing by creating a list of numbers from 1 to 10. It extracts the first five elements and then creates a new list with these elements reversed, printing all three lists.

### Code
```python
lst = list(range(1, 11))

first_5 = lst[ : 5]
reverse_first_5 = first_5[ : : -1]
print(f"Original List: {lst}")
print(f"Extracted first five elements: {first_5}")
print(f"Reversed extracted element: {reverse_first_5}")
```

### Output
```
Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted element: [5, 4, 3, 2, 1]
```
