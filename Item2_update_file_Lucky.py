# Item 2
def update_file(file_to_update):

    dictionary_file = load_csv_file_to_dictionary(file_to_update)

    print("Enter 1 - to add a New Student\n" +
          "Enter 2 - to modify a student Name\n" +
          "Enter 3 - to modify a student Mark\n" +
          "Enter 4 - to remove a Student\n" +
          "Enter 0 - to exit\n")
    choice = int(get_non_empty_input("Enter a selection: \n"))

    while choice != 0:
        if choice == 1:
            new_student_name = get_non_empty_input("Enter New Student Name: \n")
            id = get_non_empty_input("Enter Student ID: \n")
            marks = get_non_empty_input("Enter Student Marks: \n")
            grade = calculate_letter_grade(float(marks))

            dictionary_file[id] = {}
            dictionary_file[id]["Student Name"] = new_student_name
            dictionary_file[id]["Final Marks"] = marks
            dictionary_file[id]["Final Grade"] = grade
            write_from_dictionary_to_file(dictionary_file,file_to_update)

        elif choice == 2:
            key_id = get_non_empty_input("Enter the Student ID: \n")
            if key_id in dictionary_file:
                dictionary_file[key_id]["Student Name"] = get_non_empty_input("Enter the new student name: \n")
                write_from_dictionary_to_file(dictionary_file, file_to_update)

        elif choice == 3:
            key_id = get_non_empty_input("Enter the Student ID: \n")
            if key_id in dictionary_file:
                dictionary_file[key_id]["Final Marks"] = get_non_empty_input("Enter the new marks: \n")
                write_from_dictionary_to_file(dictionary_file, file_to_update)

        elif choice == 4:
            key_id = get_non_empty_input("Enter the Student ID: \n")
            remove_a_student(file_to_update, key_id)
