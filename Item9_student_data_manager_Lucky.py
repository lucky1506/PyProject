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

    # check for entry is a digit only. if not digit, return 1 to prompt invalid selection
    if is_all_digit(user_input) == False:
        print("\nInvalid selection.\n")
        return 1

    # convert the user_input to int since the input function reads input as string
    user_input = int(user_input)

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
        print("Invalid entry.")
    # otherwise entry is 0-6, return 3
    return 3  # valid selection and entry = 1 to 6
