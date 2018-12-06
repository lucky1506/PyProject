#  Item 8
def is_all_digit(user_input):
    """
    This function validates user entry.
    It checks entry is only digits from
    0 to 9, and no other characters.
    """
    numbers = "0123456789"
    for character in user_input:
        if character not in numbers:
            return False
    return True


#  Item 7
def calculate_letter_grade(marks):
    """
        This function calculates  and returns the letter
        grade following the rules below:

        >=85% - A
        >=75% and <85% - B
        >=65% and <75% - C
        >=50% and <65% - D
        <50% - F
    """

    if marks < 50:
        return "F"
    elif marks >= 50 and marks < 65:
        return "D"
    elif marks >= 65 and marks < 75:
        return "C"
    elif marks >= 75 and marks < 85:
        return "B"
    elif marks >= 85:
        return "A"


#  Item 1
def create_new_file(file_name):
    """
    This function takes a name for a file and creates a new student data file
    with comma separated 4 columns, and with its 1st row as the header for
    Student Name, ID, Marks and Letter Grade. User may enter student data in
    this new file before closing or quit to close the new file.
    """

    new_file = open(file_name, "w")
    print("\nYou have created a new file named: " + file_name + "\n")
    # write the 1st row which is the Header in 4 columns
    new_file.write("Student_Name,ID,Marks,Grade\n")
    entry = int(input("Do you want to enter data? (enter: 1 for Yes, 0 to Exit): \n"))

    while entry != 0:
        student_name = input("Enter Student Name: \n")
        id = input("Enter Student ID: \n")
        marks = input("Enter Student Marks: \n")
        grade = calculate_letter_grade(float(marks))
        new_file.write(student_name + "," + id + "," + marks + "," + grade + "\n")
        print("You entered: Student Name: " + student_name + ", Student ID: " + id +
              ", Student Marks: " + marks + ", Letter Grade: " + grade + "\n")
        entry = int(input("Do you want to enter another data? (enter: 1 for Yes, 0 to Exit): "))
    new_file.close()


# Item 2
def update_file(file_to_update):
    return "Need to Complete"

# Item 3
def remove_a_student(remove_from_file, remove_id):
    return "Need to Complete"


# Item 4
def search_student(search_in_file, student_lookup):
    return "Need to Complete"


# Item 5
def file_summary(file_to_summarize):
    return "Need to Complete"


# Item 6
def print_all(file_to_print):
    return "Need to Complete"


#  Item 9
def student_data_manager(user_input):
    """ This function takes in the user input and checks:
        1) for valid menu selections that is only digits
        2) if valid, processes user input by calling other functions
        3) if not valid, prompts for correct entry

        Returns 1 : if invalid selection (not digits)
        Returns 2:  if valid selection and entry = 0
        Returns 3:  if valid selection and entry = 1 to 6
    """

    # check for valid menu selections
    if is_all_digit(user_input) == False:
        print("\nInvalid selection.\n")
        return 1  # invalid selection

    # convert the user_input to int since the input function reads input as string
    user_input = int(user_input)

    # check if user_inputs are only 0,1,2,3,4,5,6
    if user_input in [0, 1, 2, 3, 4, 5, 6]:

        # exit program
        if user_input == 0:
            print("\nYou selected 0 to quit. Goodbye!")
            return 2  # Valid selection and entry = 0 to quit

        # Create File
        elif user_input == 1:
            new_file_name = input("Name your new file: ")
            create_new_file(new_file_name)

        #  Update File
        elif user_input == 2:
            file_to_update = input("Enter the file name you want to update: ")
            update_file(file_to_update)

        #  Remove Student
        elif user_input == 3:
            remove_from_file = input("Enter the file name to remove a student from: ")
            remove_id = input("Enter Student ID you wish to remove: ")
            remove_a_student(remove_from_file, remove_id)

        #  Search Student
        elif user_input == 4:
            search_in_file = input("Enter a file name to search for the student: ")
            student_lookup = input("Enter Student ID you wish to look up: ")
            search_student(search_in_file, student_lookup)

        #  Print Summary
        # summarizes number of students, Average Marks, number of As Bs etc in a file
        elif user_input == 5:
            file_to_summarize = input("Enter file name to print summary: ")
            file_summary(file_to_summarize)

        # Print All:  prints max 20 lines of student data at a time (row by row)
        elif user_input == 6:
            file_to_print = input("Enter file name to print all (20 student data/page): ")
            print_all(file_to_print)

    else:
        print("Invalid entry.")

    return 3  # valid selection and entry = 1 to 6



def main():
    """ This is the main function(). It prints out the main MENU of the database app,
        prompts the users for a menu selection and reads and passes the user entry to
        the student_data_manager function for processing the menu selection.
    """
    while True:

        print("\n")
        print("***************************************************************************")
        print("*    Selection        M    E    N    U                                    *")
        print("***************************************************************************")
        print("*        1      -     Create a new Student data file                      *\n" +
              "*        2      -     Update an existing student data file                *\n" +
              "*        3      -     Remove a student                                    *\n" +
              "*        4      -     Search a student                                    *\n" +
              "*        5      -     Print only a summery of student data                *\n" +
              "*        6      -     Print the entire student data file to command line  *\n" +
              "*        0      -     Quit                                                *\n" +
              "***************************************************************************\n")
        print("Welcome to Student Database System!")
        read_entry = input("Enter a selection from the menu (Or 0 to quit): ")
        if student_data_manager(read_entry) == 2:
            break


main()