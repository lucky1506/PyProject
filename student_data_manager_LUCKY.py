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

        if user_input == 0:
            print("\nYou selected 0 to quit. Goodbye!")
            return 2  # Valid selection and entry = 0 to quit

        elif user_input == 1:
            new_file_name = input("Name your new file: ")
            create_new_file(new_file_name)

        elif user_input == 2:
            file_to_update = input("Enter the file name you want to update: ")
            update_file(file_to_update)

        elif user_input == 3:
            remove_student_from_file = input("Enter the file name to remove a student from: ")
            remove_to_student = input("Enter Student ID you wish to remove: ")
            remove_student(remove_student_from_file, remove_to_student)

        elif user_input == 4:
            search_student_in_file = input("Enter a file name to search for the student: ")
            student_lookup = input("Enter Student ID you wish to look up: ")
            search_student(search_student_in_file, student_lookup)

        # print summary of a student data file: number of students, Average Marks, number of As Bs etc...
        elif user_input == 5:
            summarize_file = input("Enter file name to print summary: ")
            file_summary(summarize_file)

        # prints max 20 student data at a time (row by row)
        elif user_input == 6:
            file_to_print = input("Enter file name to print all (20 student data/page): ")
            print_all(file_to_print)

    else:
        print("Invalid entry.")

    return 3  # valid selection and entry = 1 to 6
