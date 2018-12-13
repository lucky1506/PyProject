# Item 4 - Search ID (Lucky)
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
