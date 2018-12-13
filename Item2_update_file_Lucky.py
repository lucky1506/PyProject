# Item 2
def update_file(file_to_update):
    dictionary_file = load_csv_file_to_dictionary(file_to_update)
    print("Enter 1 - to add a New Student\n" +
          "Enter 2 - to modify a student Name\n" +
          "Enter 3 - to modify a student Mark\n" +
          "Enter 4 - to remove a Student\n" +
          "Enter 0 - to exit\n")
    choice = input("Enter a selection: \n")

    # check if entry is a digit only. if not digit, return 1 to prompt invalid selection
    if is_all_digit(choice) == False:
        print("\nInvalid selection.\n")
        return 1

    choice = int(choice)
    # check if entry is any of these digits 0,1,2,3,4
    if choice in [0, 1, 2, 3, 4]:
        if choice == 0:
            print("\nYou selected 0 to quit. Goodbye!")
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

                print("You added: Student Name: " + new_student_name + ", Student ID: " + id +
                      ", Student Marks: " + marks + ", Letter Grade: " + grade + "\n")
                entry = input("Do you want to add another student? (enter: Y or N ): ")

                if entry not in "Yy":
                    print("Invalid response. Try again.")
                    break

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
