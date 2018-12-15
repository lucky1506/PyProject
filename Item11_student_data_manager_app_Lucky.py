# Item 11 All -- Student Data Manager App (COMBINED)


# Item 5
def file_summary(file_to_summarize):
    pass


# Item 6
def print_all(file_to_print):
    pass


#  Item 14
def get_non_empty_input(question):
    """ This function checks for non empty input and prompts
    the user to enter a data """
    value = input(question)
    value = value.strip()
    while value == "":
        print("No value entered. Please enter a value.")
        value = input(question)
        value = value.strip()
    return value


#  Item 13
def write_from_dictionary_to_file(d_file, filename):
    """ This method writes comma separated values from dictionary to file"""

    # open the file in write mode
    f = open(filename, "w")
    f.write("Student Name,ID,Marks,Grade\n")

    # if the id (key) exists in the dictionary, write the key and values in the file
    for key in d_file:
        value = d_file[key]
        f.write(value["Student Name"] + "," + key + "," + str(value["Final Marks"]) + "," + value["Final Grade"] + "\n")
    f.close()


#  Item 12
def load_csv_file_to_dictionary(f_name):
    student_id_data = {}
    f = open(f_name, "r")
    lines = f.readlines()
    f.close()
    data_lines = lines[1:]

    for line in data_lines:
        line = line.strip()
        words = line.split(",")
        student_names = words[0]
        student_id = words[1]
        final_marks = float(words[2])
        final_grade = words[3]
        student_id_data[student_id] = {}
        student_id_data[student_id]["Student Name"] = student_names
        student_id_data[student_id]["Final Marks"] = final_marks
        student_id_data[student_id]["Final Grade"] = final_grade
    return student_id_data


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


# Item 4_Search (Lucky)

def search_student(search_file, id_lookup):
    """
    This function takes a file name and an id to search
    a student in the file. First it reads the data from
    the file in a dictionary in memory. Then it looks for
    id in in the dictionary. It returns the search result.
    It allows the user to searc for another student in the
    same file, or exit to main menu.
    """

    dictionary_file = load_csv_file_to_dictionary(search_file)

    if id_lookup in dictionary_file:
        name = dictionary_file[id_lookup]["Student Name"]
        write_from_dictionary_to_file(dictionary_file, search_file)
        print("\nStudent Id: " + str(
            id_lookup) + ", Student Name: " + name + " exists in file name: " + search_file + ".\n")

    else:
        print("\nStudent Id " + id_lookup + " does not exist.\n")


# Item 3
def remove_a_student(remove_from_file, remove_id):
    dictionary_file = load_csv_file_to_dictionary(remove_from_file)

    if remove_id in dictionary_file:
        name = dictionary_file[remove_id]["Student Name"]
        del dictionary_file[remove_id]
        write_from_dictionary_to_file(dictionary_file, remove_from_file)
        print("\nStudent: " + str(remove_id) + ", " + name + " is removed from file: " + remove_from_file + ".\n")
    else:
        print("\nId " + remove_id + "not found.\n")


# Item 2
def update_file(file_to_update):
    """ This function allows users to add a new student to an existing file,
        or update an existing student name, or update an existing student
        final marks, or to remove an existing student from a file.
    """

    dictionary_file = load_csv_file_to_dictionary(file_to_update)
    while True:
        print("\n****************************************")
        print("Enter 1 - to add a New Student\n" +
              "Enter 2 - to modify a student Name\n" +
              "Enter 3 - to modify a student Mark\n" +
              "Enter 4 - to remove a Student\n" +
              "Enter 0 - to return to Main Menu")
        print("****************************************")
        choice = input("Enter a selection: \n")

        # check if entry is a digit only. if not digit, return 1 to prompt invalid selection
        if is_all_digit(choice) == False:
            print("Invalid selection.\n")
            continue



        # if entry is any of these digits 0,1,2,3,4
        if choice in ["0", "1", "2", "3", "4"]:
            choice = int(choice)

            #  Return to main menu if 0
            if choice == 0:
                print("You entered 0 to return to the main Menu!")
                return 2
            elif choice == 1:
                while True:
                    new_student_name = get_non_empty_input("Enter New Student Name: \n")
                    id = get_non_empty_input("Enter Student ID: \n")
                    marks = get_non_empty_input("Enter Student Marks: \n")
                    grade = calculate_letter_grade(float(marks))

                    dictionary_file[id] = {}
                    dictionary_file[id]["Student Name"] = new_student_name
                    dictionary_file[id]["Final Marks"] = marks
                    dictionary_file[id]["Final Grade"] = grade

                    write_from_dictionary_to_file(dictionary_file, file_to_update)

                    print("\nYou added: Student Name: " + new_student_name + ", Student ID: " + id +
                          ", Student Marks: " + marks + ", Letter Grade: " + grade + "\n")
                    entry = input("\nDo you want to add another student? (enter: Y or N ): ")

                    if entry not in "Yy":
                        print("Invalid response. Try again.\n")
                        break

            elif choice == 2:
                key_id = get_non_empty_input("Enter the Student ID: \n")
                if key_id in dictionary_file:
                    dictionary_file[key_id]["Student Name"] = get_non_empty_input("\nEnter the new student name: \n")
                    write_from_dictionary_to_file(dictionary_file, file_to_update)

            elif choice == 3:
                key_id = get_non_empty_input("\nEnter the Student ID: \n")
                if key_id in dictionary_file:
                    dictionary_file[key_id]["Final Marks"] = get_non_empty_input("\nEnter the new marks: \n")
                    write_from_dictionary_to_file(dictionary_file, file_to_update)

            elif choice == 4:
                key_id = get_non_empty_input("\nEnter the Student ID: \n")
                remove_a_student(file_to_update, key_id)

            # if input is one of the selections
            break

        else:
            print("Invalid selection. Try again.")











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


#  Item 9
def student_data_manager(user_input):
    """ This function takes in  user input and checks:
        1) for input is only a digit
        2) if digit, it checks if inputs are valid menu selections: only 0 - 6
        3) if not valid, prompts for correct entry

        Returns 1 : if input is not digit (invalid case)
        Returns 2:  if input is 0 (selection to quit program)
        Returns 3:  if input is any digit from 1 to 6 (valid menu selection)
    """
    #  return 1
    # check for entry is a digit only. if not digit, return 1 to prompt invalid selection
    if is_all_digit(user_input) == False:
        print("\nInvalid selection.\n")
        return 1

    # convert the user_input to int since the input function reads input as string
    user_input = int(user_input)

    #  return 2
    # check if entry is any of these digits 0,1,2,3,4,5,6
    if user_input in [0, 1, 2, 3, 4, 5, 6]:

        # if entry is 0, return 2 to exit program
        if user_input == 0:
            print("\nYou selected 0 to quit. Goodbye!")
            return 2

        #  if entry is 1: Create a new file
        elif user_input == 1:
            new_file_name = input("Name your new file: ")
            create_new_file(new_file_name)


        #  if entry is 2: Update an existing File
        elif user_input == 2:
            file_to_update = input("Enter the file name to update (or press enter to cancel): ")
            if file_to_update != "":
                update_file(file_to_update)

        #  if entry is 3: Remove a Student from a file
        elif user_input == 3:
            remove_from_file = input("Enter the file name to remove a student from (or press enter to cancel): ")
            if remove_from_file != "":
                remove_id = input("Enter Student ID you wish to remove (or press enter to cancel): ")
                if remove_id != "":
                    remove_a_student(remove_from_file, remove_id)

        #  if entry is 4: Search a Student in a file
        elif user_input == 4:
            search_in_file = input("Enter a file name to search for the student (or press enter to cancel): ")
            if search_in_file != "":
                student_lookup = input("Enter Student ID you wish to look up (or press enter to cancel): ")
                if student_lookup != "":
                    search_student(search_in_file, student_lookup)

        #  if entry is 5: Print Summary of students, Average Marks, number of As Bs etc from a file
        elif user_input == 5:
            file_to_summarize = input("Enter file name to print summary(or press enter to cancel): ")
            if file_to_summarize != "":
                file_summary(file_to_summarize)

        # if entry is 6: print max 20 lines of student data at a time (row by row) per page
        elif user_input == 6:
            file_to_print = input("Enter file name to print 20 student data/page (or press enter to cancel): ")
            if file_to_print != "":
                print_all(file_to_print)

    # if entry is none of these digits 0,1,2,3,4,5,6
    else:
        print("Invalid entry. Try again or enter 0 to quit.")

    #  return 3 for entry being valid: 0-6
    return 3  # valid selection and entry = 1 to 6


#  Item 10
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
