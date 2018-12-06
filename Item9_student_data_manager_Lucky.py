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