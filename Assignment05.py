# -------------------------------------------------------------------------- #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files,
#       and exception handling
# Change Log: (Who, When, What)
#   Brin Masterson, 2023-11-07, Created Script
#   Brin Masterson, 2023-11-11, Started switch to dictionaries
#   Brin Masterson, 2023-11-12, Worked on changes for JSON
#   Brin Masterson, 2023-11-13, Added Error handling change
#
# -------------------------------------------------------------------------- #
# Setup Code
import json

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

MENU: str = f"""
---- Course Registration Program ----
Select from the following menu:
1. Register a Student for a Course
2. Show current data
3. Save data to the {FILE_NAME} file
4. Exit the program
--------------------------------------
"""

# Define the Data Variables
student_first_name: str = ""  # Holds the first name of student (user input).
student_last_name: str = ""  # Holds the last name of student (user input).
course_name: str = ""  # Holds the course name (user input).
json_data: str = ""  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str = ""  # Holds the user menu selection value (user input).
student_data: dict[str, str, str] = {}  # Holds student data as a dictionary (first,last,course names)
students: list[dict[str]] = []  # Table of student data.

# -------------------------------------------------------------------------- #
# Main Body

# Open the JSON file for reading
try:
	f = open('SomeFile.txt', 'r')
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except ZeroDivisionError as e:
	print("Please do not use Zero for the second number!\n")
	print("Built-In Python error info: ")
	print(e, e.__doc__, type(e), sep='\n')
except FileNotFoundError as e:
	print("Text file must exist before running this script!]\n")
	print("Built-In Python error info: ")
	print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
	print("There was a non-specific error!\n")
	print("Built-In Python error info: ")
	print(e, e.__doc__, type(e), sep='\n')


# Present and Process the data
while True:
    print()  # blank row(s) for readability
    # Present the menu of choices
    menu_choice = input(f"{MENU}\nWhat would you like to do? ").strip()
    print()  # blank row(s) for readability

    # Input student data
    if menu_choice == "1":
        except Exception as e:
        print("Error! Please check you are not dividing by zero.\n")
        print("-- Technical Error Message -- ")
        print(e)  # Print the exception object (typically includes the error message)print(type(e))
        # Print the type of the exception objectprint(e.__doc__)
        # Print the documentation string of the exception typeprint(e.__str__())
        # Print the string representation of the exception

        student_first_name = input("Enter the student's first name: ").strip()
        student_last_name = input("Enter the student's last name: ").strip()
        course_name = input("Enter the course name: ").strip().capitalize()

        # Store student details in dictionary
        student_data = {
            "First Name": student_first_name,
            "Last Name": student_last_name,
            "Course Name": course_name
        }

        # Add student details dictionary to table
        students.append(student_data)

        # Confirm registration
        print()
        print(
            f"{student_first_name} {student_last_name} is registered for {course_name}."
        )
        print()

        continue

    # Present current data
    elif menu_choice == "2":

        # Present the current data
        print("The current student registration data is: ")
        print("--Course Name, Last Name, First Name--")
        for each_row in students:
            print(
                f'{each_row["Course Name"]}, '
                f'{each_row["Last Name"]}, '
                f'{each_row["First Name"]}'
            )
        continue

    # Save data to a file
    elif menu_choice == "3":
        # Save the data to the file
        file = open(FILE_NAME, "w")
        json.dump(students, file)
        file.close()

        # Display saved data
        print(f"{FILE_NAME} has been saved as:\n")
        print("--Course Name, Last Name, First Name--")
        for each_row in students:
            # display data
            print(f'{each_row["Course Name"]},'
                  f'{each_row["Last Name"]},'
                  f'{each_row["First Name"]}'
                  )
        continue

    # Exit program
    elif menu_choice == "4":
        # Stop the loop and exit program
        print("Okay, byeeeee!")
        quit()

    # Handling those who go rogue
    else:
        print("OK OK we get it... you're a rule breaker. Try again!")
        break
