# -------------------------------------------------------------------------- #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files,
#       and exception handling
# Change Log: (Who, When, What)
#   Brin Masterson, 2023-11-07, Created Script
#   Brin Masterson, 2023-11-11, Started switch to dictionaries
#   Brin Masterson, 2023-11-12, Worked on changes for JSON
#   Brin Masterson, 2023-11-13, Added Error handling change, connected to GitHub,
#   Brin Masterson, 2023-11-13, (cont.) Comment cleanup and format tidying.
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
student_data: dict[str, str, str] = {}  # Holds student data as a dictionary
students: list[dict[str]] = []  # Table of student data.

# -------------------------------------------------------------------------- #
# Main Body
# Get existing data from JSON file, load into table
# Error handling when the file is read into the list of dictionary rows.
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
except FileNotFoundError as e:
    print(f"\nThe {FILE_NAME} file must exist before running this script.\n")
    print(" -- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    print("\nThe program will now exit. \n")
    exit()
except Exception as e:
    print("\nThere was a non-specific error! \n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    print("\nThe program will now exit. \n")
    exit()
else:
    if not file.closed:
        file.close()

# Present and Process the data
while True:
    # Present the menu of choices
    menu_choice = input(f"\n{MENU}\nWhat would you like to do? \n").strip()

    # Input student data
    if menu_choice == "1":
        # Error handling when the user enters a first and last names
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name.isalpha():
                raise ValueError(f"\nThe first name should not contain numbers.\n\n")

            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name.isalpha():
                raise ValueError(f"\nThe last name should not contain numbers.\n\n")

        except ValueError as e:
            print(e)  # Prints the custom message
            print(" -- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())

        except Exception as e:
            print("\nThere was a non-specific error :(\n")
            print(" -- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        else:
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
            print(
                f"\n{student_first_name} {student_last_name} "
                f"is registered for {course_name}.\n"
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
        file = open(FILE_NAME, "w")
        # Open file and write data, close to save
        # Error handling when the dictionary rows are written to the file
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)

        except FileNotFoundError as e:
            print(f"The {FILE_NAME} file must exist before running this script\n")
            print(" -- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')

        except Exception as e:
            print("There was a non-specific error!\n")
            print(" -- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file.closed:
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
