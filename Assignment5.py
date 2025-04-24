#Answers for Assignment 5

#Task 1


# Create a dictionary of student names and their marks
student_marks = {
    'Alice': 85,
    'Bob': 78,
    'Charlie': 92,
    'David': 70,
    'Eva': 88
}

# Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Retrieve and display the corresponding marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")

'''
Enter the student's name: Alice
Alice's marks: 85

nter the student's name: Anes
Student not found.
'''

#Task 2


# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Extract the first five elements from the list
extracted_numbers = numbers[:5]

# Reverse the extracted elements
reversed_numbers = extracted_numbers[::-1]

# Print both the extracted list and the reversed list
print("Extracted numbers:", extracted_numbers)
print("Reversed extracted numbers:", reversed_numbers)

'''
o/p

Extracted numbers: [1, 2, 3, 4, 5]
Reversed extracted numbers: [5, 4, 3, 2, 1]
'''
