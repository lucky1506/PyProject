import os
import statistics


# ****************************************************************************
# CS 131A-Python Programming-Project  Date: December 21, 2018
# Team members: Lucky Pataky, Grace Durham, Stephanie Boyette and Katie Jones
# Fall 2018/City College of SF (ccsf.edu)
# Professor: Dr. Indika Walimuni
# ****************************************************************************


#  Item 16
def filename_check(filename):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "_.-"
    valid_first_character = alpha + alpha.upper()
    valid_characters = alpha + alpha.upper() + numbers + symbols
    first_character = filename[0]
    if first_character not in valid_first_character:
        print("\nInvalid file name. File must begin with a letter.\n")
        return False
    else:
        for c in filename:
            if c not in valid_characters:
                print("\n" + c + " is an invalid character.\n")
                print("\nFile name must start with a letter followed by any of the following:\n"
                      "letters, numbers and  .  -  _ \n")
                return False
    return True

# Item 6
def print_all(file_to_print):
    student_dic = load_csv_file_to_dictionary(file_to_print)
    the_number_of_students = len(student_dic.keys())
    all_keys = student_dic.keys()
    numpages = int(the_number_of_students / 20)
    if the_number_of_students%20 != 0:
        numpages += 1

    print('_' * 70)
    print('')
    header = 'Line No,STUDENT NAME,ID,MARKS,GRADE'
    line_num, name, idn, marks, grade = header.split(',')
    print(f'{line_num:^10}{name:<30}{idn:^10}{marks:^10}{grade:^10}')
    print('_' * 70)
    print('')

    line_count = 1
    page = 1

    while True:
        line_count = 1
        for student_id in all_keys:
            if line_count <= 20*page and line_count>20*(page-1):
                name = student_dic[student_id]["Student Name"]
                marks = student_dic[student_id]["Final Marks"]
                grade = student_dic[student_id]["Final Grade"]
                print(f'{line_count:^10}{name:<30}{student_id:^10}{marks:^10}{grade:^10}')
            line_count += 1

        if page <numpages:
            choice = input("\nPrint next 20? (Type 1 for Yes, Or press enter to Exit): \n")
            if choice == "1":
                page = page + 1
            else:
                break
        else:
            break


# Item5
def print_only_summary_of_student_data(fname):
    """ This function prints a summary of a student data file """

    student_dic = load_csv_file_to_dictionary(fname)
    the_number_of_students = len(student_dic.keys())

    print("\n")
    print("                         FILE SUMMARY                                      ")
    print("______________________________________________________________________")
    print("The number of students:", the_number_of_students)
    final_marks_list = []
    final_grade_list = []

    for key, value in student_dic.items():
        for k, v in value.items():
            if k == "Final Marks":
                final_marks_list.append(v)
            elif k == "Final Grade":
                final_grade_list.append(v)
    final_marks_sum = sum(final_marks_list)

    average_total_marks = final_marks_sum / the_number_of_students
    print("The average total marks:", average_total_marks)

    copy_of_final_marks_list = final_marks_list[:]
    copy_of_final_marks_list.sort()

    if (len(final_marks_list) % 2 == 0):
        print("The median total marks:", (
                copy_of_final_marks_list[(len(final_marks_list) - 1) // 2] + copy_of_final_marks_list[
            len(final_marks_list) // 2]) / 2)

    else:
        print("The median total marks:", copy_of_final_marks_list[len(final_marks_list) // 2])

    print("The standard deviation of the total marks:", statistics.stdev(final_marks_list))
    print("Highest marks:", max(copy_of_final_marks_list))
    print("Minimum marks:", min(copy_of_final_marks_list))
    print("Number of 'A's:", final_grade_list.count("A"))
    print("Number of 'B's:", final_grade_list.count("B"))
    print("Number of 'C's:", final_grade_list.count("C"))
    print("Number of 'D's:", final_grade_list.count("D"))
    print("Number of 'F's:", final_grade_list.count('F'))
    print("______________________________________________________________________")


#  Item 15
def does_file_exist(file_name):
    """
    This function takes in a file name or a path. It
    uses the python built-in os library functions to check
    if the file path exists and also that the path points to a
    file and not to a directory. These functions eliminates
    the need for catching exception.
    """

    while True:
        if file_name != "":
            if os.path.exists(file_name) and os.path.isfile(file_name):
                return file_name
            else:
                file_name = input(
                    "\nThat file does not exist.\n\nEnter an existing file name (or press enter to cancel): ")
        else:
            print("\nYou exit to the main menu.")
            return None


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

    # open file in write mode and write the header
    f = open(filename, "w")
    f.write("Student Name,ID,Marks,Grade\n")

    # if id (key) exists in dictionary, write key and values to file
    for key in d_file:
        value = d_file[key]
        f.write(value["Student Name"] + "," + key + "," + str(value["Final Marks"]) + "," + value["Final Grade"] + "\n")
    f.close()


#  Item 12
def load_csv_file_to_dictionary(f_name):
    """
    This function opens a csv file and stores data from the
    file into a dictionary in memory using student ID as the key.
    """

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


# Item 4_Search
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
    """
    This function takes an ID and a file name and removes the
    student data by that id from the given file. It prints
    the removed student's name and ID after removing.
    """

    dictionary_file = load_csv_file_to_dictionary(remove_from_file)

    if remove_id in dictionary_file:
        name = dictionary_file[remove_id]["Student Name"]
        del dictionary_file[remove_id]
        write_from_dictionary_to_file(dictionary_file, remove_from_file)
        print("\nStudent: " + str(remove_id) + ", " + name + " is removed from file: " + remove_from_file + ".\n")
    else:
        print("\nId " + remove_id + " not found.\n")


# Item 2
def update_file(f_csv):
    """ This function allows users to add a new student to an existing file,
        or update an existing student name, or update an existing student
        final marks, or to remove an existing student from a file.
    """

    dictionary_d = load_csv_file_to_dictionary(f_csv)
    while True:
        print("\n****************************************")
        print("Enter 1 - to add a New Student\n" +
              "Enter 2 - to modify a student Name\n" +
              "Enter 3 - to modify a student Mark\n" +
              "Enter 4 - to remove a Student\n" +
              "Enter 0 - to return to Main Menu")
        print("****************************************")
        choice = input("Enter a selection: \n")

        # if entry is not digit, return 1 to print invalid selection
        if is_all_digit(choice) == False:
            print("Invalid selection. Select a number from the menu..\n")
            continue

        if choice in ["0", "1", "2", "3", "4"]:
            choice = int(choice)

            #  0 - Return to main menu
            if choice == 0:
                print("You entered 0 to return to the main Menu!")
                return 2

            # 1 - add a new student
            elif choice == 1:
                while True:
                    id = get_non_empty_input("Enter Student ID: \n")
                    if id in dictionary_d:
                        print("That ID already exists in this file.\n")
                        continue

                    new_student_name = get_non_empty_input("Enter New Student Name: \n")

                    while True:
                        marks = get_non_empty_input("Enter Student Marks: \n")
                        try:
                            marks = float(marks)
                            break
                        except:
                            print("Marks must be all numbers or a decimal value.  ")
                    grade = calculate_letter_grade(marks)

                    dictionary_d[id] = {}
                    dictionary_d[id]["Student Name"] = new_student_name
                    dictionary_d[id]["Final Marks"] = marks
                    dictionary_d[id]["Final Grade"] = grade

                    write_from_dictionary_to_file(dictionary_d, f_csv)

                    print("\nYou added: Student Name: " + new_student_name + ", Student ID: " + id +
                          ", Student Marks: " + str(marks) + ", Letter Grade: " + grade + "\n")
                    entry = input("\nDo you want to add another student? (Y for yes or any key to exit): ")

                    if entry in "Yy" and entry != "":
                        continue
                    else:
                        break

            elif choice == 2:
                key_id = get_non_empty_input("Enter Student ID: \n")
                if key_id in dictionary_d:
                    dictionary_d[key_id]["Student Name"] = get_non_empty_input("\nEnter the new student name: \n")
                    write_from_dictionary_to_file(dictionary_d, f_csv)
                else:
                    print("ID does not exist.")

            elif choice == 3:
                key_id = get_non_empty_input("\nEnter Student ID: \n")
                if key_id in dictionary_d:

                    while True:
                        new_marks = get_non_empty_input("Enter the new marks: \n")
                        try:
                            new_marks = float(new_marks)
                            break
                        except:
                            print("Marks must be all numbers or a decimal value.  ")
                    new_grade = calculate_letter_grade(new_marks)

                    dictionary_d[key_id]["Final Marks"] = new_marks
                    dictionary_d[key_id]["Final Grade"] = new_grade
                    write_from_dictionary_to_file(dictionary_d, f_csv)
                else:
                    print("ID does not exist.")

            elif choice == 4:
                key_id = get_non_empty_input("\nEnter the Student ID: \n")
                remove_a_student(f_csv, key_id)

            # if input is one of the selections
            break
        else:
            print("\nInvalid selection. Select a number from the menu.")


#  Item 1 - create new csv file
def create_new_file(file_name):
    """
    This function takes a name for a file and creates a new student data file
    with comma separated 4 columns, and with its 1st row as the header for
    Student Name, ID, Marks and Letter Grade. User may enter student data in
    this new file before closing or quit to close the new file.
    """

    new_file = open(file_name, "w")
    print("\nYou have created a new file named: " + file_name + "\n")

    # write row1: Header
    new_file.write("Student_Name,ID,Marks,Grade\n")
    entry = input("Do you want to enter data? (enter: 1 for Yes, or enter any key to Exit): \n")

    while entry == "1":

        #  Users are allowed to exit only at the beginning of the data entry phase.
        #  After an ID is entered, they must continue. The entries can be updated after they are done.
        id = input("Enter Student ID (or press enter to cancel): \n")
        if id == "":
            break

        student_name = input("Enter Student Name: \n")

        while True:
            marks = input("Enter Student Marks: \n")
            try:
                marks = float(marks)
                break
            except:
                print("Marks must be all numbers or a decimal value.  ")

        grade = calculate_letter_grade(marks)

        new_file.write(student_name + "," + id + "," + str(marks) + "," + grade + "\n")
        print("You entered: Student Name: " + student_name + ", Student ID: " + id +
              ", Student Marks: " + str(marks) + ", Letter Grade: " + grade + "\n")

        entry = input("Do you want to enter another data? (enter: 1 for Yes, or enter any key to Exit): ")
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

    # if selection is not digit (return 1. invalid entry)
    if is_all_digit(user_input) == False:
        print("\nInvalid selection. Select a number from the menu.\n")
        return 1

    #  correct selection "0-6"
    if user_input in ["0", "1", "2", "3", "4", "5", "6"]:

        # convert the user_input to int since the input function reads input as string
        user_input = int(user_input)

        # selection 0, return 2 to exit program
        if user_input == 0:
            print("\nYou selected 0 to quit. Goodbye!")
            return 2

        #  selection 1: Create a new file

        elif user_input == 1:
            while True:
                new_file_name = input("Name your new file (or press enter to cancel): ")
                if new_file_name != "" and filename_check(new_file_name):
                    create_new_file(new_file_name)
                    break
                elif new_file_name == "":
                    break

        #  selection 2: Update an existing file
        elif user_input == 2:
            file_to_update = input("Enter the file name to update (or press enter to cancel): ")
            valid_file = does_file_exist(file_to_update)
            if valid_file != None:
                update_file(valid_file)

        #  selection 3: Remove a Student
        elif user_input == 3:
            remove_from_file = input("Enter the file name to remove a student from (or press enter to cancel): ")

            valid_file = does_file_exist(remove_from_file)

            if valid_file != None:
                remove_id = input("Enter Student ID you wish to remove (or press enter to cancel): ")
                if remove_id != "":
                    remove_a_student(valid_file, remove_id)

        #  selection 4: Search a student
        elif user_input == 4:
            search_in_file = input("Enter a file name to search for a student (or press enter to cancel): ")

            valid_file = does_file_exist(search_in_file)

            if valid_file != None:
                student_lookup = input("Enter Student ID to look up (or press enter to cancel): ")
                if student_lookup != "":
                    search_student(valid_file, student_lookup)

        #  selection 5: Print Summary of students, Average Marks, number of As Bs etc from a file
        elif user_input == 5:
            file_to_summarize = input("Enter file name to print summary(or press enter to cancel): ")

            valid_file = does_file_exist(file_to_summarize)
            if valid_file != None:
                print_only_summary_of_student_data(valid_file)

        # selection 6: print max 20 lines of student data at a time (row by row) per page
        elif user_input == 6:
            file_to_print = input("Enter file name to print 20 student data/page (or press enter to cancel): ")
            valid_file = does_file_exist(file_to_print)
            if valid_file != None:
                print_all(valid_file)


    # invalid main menu selection(not 0,1,2,3,4,5,6)
    else:
        print("\nInvalid selection. Select a number from the menu.")

    #  return 3 for valid 0-6 selection
    return 3


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
              "*        5      -     Print only a summary of student data                *\n" +
              "*        6      -     Print the entire student data file to command line  *\n" +
              "*        0      -     Quit                                                *\n" +
              "***************************************************************************\n")
        print("Welcome to Student Database System!")
        read_entry = input("Enter a selection from the menu (Or 0 to quit): ")
        if student_data_manager(read_entry) == 2:
            break


main()
