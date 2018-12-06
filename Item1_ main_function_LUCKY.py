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