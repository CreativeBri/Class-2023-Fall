# -------------------------------------------------------------------------- #
# Title: Assignment07
# Desc: This assignment demonstrates using of functions, classes
# Change Log: (Who, When, What)
#   BMasterson, 2023-11-18, Created Script
#   BMasterson, 2023-11-19, Worked on functions and organizing
#   BMasterson, 2023-11-20, Troubleshooting functions, adding descriptions
#
# -------------------------------------------------------------------------- #
# Setup Code
from json import JSONDecodeError
import json

# Constants
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

# Variables
students: list = []  # Table of student data (list of dictionary rows)
menu_choice: str = ""  # Holds the user menu selection value (user input)


# -------------------------------------------------------------------------- #
# Classes
# Processing Classes --------------------------------------- #
class FileProcessor:
    """
        Functions to read and write data between a file and a list.
        ChangeLog: (Who, When, What)
        BMasterson, 2023-11-18, Created Class
        BMasterson, 2023-11-19, Populated Class with functions
        BMasterson, 2023-11-20, Edited functions, cleaned up formatting
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Reads data from json into table.
        :param file_name: name of json file with enrollments
        :param student_data: empty table of student details
        :return: student data to populate students table
        """
        file: json = None
        try:
            file = open(file_name, 'r')
            student_data = json.load(file)
        except FileNotFoundError as e:
            IO.output_error_messages('File not found.', e)
            print('Creating file as it does not exist.')
            file = open(file_name, 'w')
            json.dump(student_data, file)
        except JSONDecodeError as e:
            IO.output_error_messages('JSON data in file is not valid.', e)
            print('Resetting it.')
            file = open(file_name, 'w')
            json.dump(student_data, file)
        except Exception as e:
            IO.output_error_messages('An error has occurred.', e)
        finally:
            if file and not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
         Writes data to json file from list.
        :param file_name: name of file
        :param student_data: table of students data
        :return: none
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)

            # Present the current data
            print()
            print("The current file data is: ")
            print("--Course Name, Last Name, First Name--")
            print("_" * 50)
            for each_student in student_data:
                print(
                    f'{each_student["CourseName"]}, '
                    f'{each_student["LastName"]}, '
                    f'{each_student["FirstName"]}'
                )
            print("_" * 50, '\n\n')

            file.close()
        except TypeError as e:
            IO.output_error_messages(
                "Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages(
                "There was a non-specific error!", e)
        finally:
            if file and not file.closed:
                file.close()


# Presentation Classes --------------------------------------- #
class IO:

    # ---- Input ------ #
    @staticmethod
    def input_menu_choice():
        """
        Collects user selection from menu options.
        :return: user's choice
        """
        choice = "0"
        try:
            choice = input(f"\nWhat would you like to do? \n").strip()
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """
        Function to capture student details from user, add to table of students.
        :param student_data: existing table of student info
        :return: updated table of student info
        """
        # Input the data
        # Error handling when the user enters a first and last names
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name.isalpha():
                raise ValueError(f"\nThe first name should only contain letters.\n\n")

            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name.isalpha():
                raise ValueError(f"\nThe last name should only contain letters.\n\n")

            course_name = input("Enter the course name: ").strip().capitalize()

            # Store student details in dictionary
            student_details = {
                "FirstName": student_first_name,
                "LastName": student_last_name,
                "CourseName": course_name
            }
            student_data.append(student_details)

            print()
            print(f'{student_first_name} {student_last_name} has been added to {course_name}.')
            print("_" * 50, '\n\n')

        except ValueError as e:
            print()
            IO.output_error_messages("Incorrect data type.", e)
        except Exception as e:
            print()
            IO.output_error_messages("There was a non-specific error", e)
        return student_data

    # ---- Output ------ #
    @staticmethod
    def output_menu(menu: str):
        """
        Present the menu of choices to the user.
        :return: none
        """
        print(menu)

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Function to display the student info in the table.
        :param student_data: table of students
        :return: none
        """
        print('\nClass Registration:')
        print("_" * 50)
        for each_student in student_data:
            message = " {} {} is registered for {}"
            print(message.format(each_student['FirstName'], each_student['LastName'], each_student['CourseName']))
        print("_" * 50, '\n\n')

    # ---- Output - Errors ------ #
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Function to display a custom error messages to the user.
        :param message: User-friendly text to display to user.
        :param error: Technical error text from system.
        :return: None
        """
        print(message)
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


# -------------------------------------------------------------------------- #
# Main body

# At start of program, load file data into a list of dictionary rows (table)
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Loop to move user through program based on user choice from menu
while True:
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()
    if menu_choice == '1':
        # Collect student details from user
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == '2':
        # Show user the current data
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == '3':
        # Save current data to file
        FileProcessor.write_data_to_file(student_data=students, file_name=FILE_NAME)
        continue

    elif menu_choice == '4':
        print()
        print('Okay, byyeee...')
        # Exit
        break

    else:
        # Users should not reach this point any longer but just in case
        print("OK OK we get it... you're a rule breaker. Try again!")
        break

print("\n-- the end --")
