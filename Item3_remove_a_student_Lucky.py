# Item 3
def remove_a_student(remove_from_file, remove_id):
    dictionary_file = load_csv_file_to_dictionary(remove_from_file)

    if remove_id in dictionary_file:
        name = dictionary_file[remove_id]["Student Name"]
        del dictionary_file[remove_id]
        write_from_dictionary_to_file(dictionary_file, remove_from_file)
        print("Student: " + str(remove_id) + ", " + name + " is removed from file: " + remove_from_file)
    else:
        print("Id " + remove_id + "not found.")
