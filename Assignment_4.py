#Task 1

# Task 1: Read a File and Handle Errors
try:
    # Open the file in read mode
    with open('/home/badhusha/Disk1/Python programs/sample.txt', 'r') as file:
        # Read and print its content line by line
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

'''
This is line 1
This is line 2
'''

#Task 2


# Task 2: Write and Append Data to a File
user_input = input("Enter some data to write to the file: ")

# Write user input to the file
with open('output.txt', 'w') as file:
    file.write(user_input + '\n')

# Append additional data
additional_data = "This is additional data appended to the file."
with open('output.txt', 'a') as file:
    file.write(additional_data + '\n')

# Read and display the final content of the file
with open('output.txt', 'r') as file:
    print("\nFinal content of the file:")
    print(file.read())

'''
This is line 1
This is line 2
Enter some data to write to the file: I am learning Python

Final content of the file:
I am learning Python
This is additional data appended to the file.

'''
