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

