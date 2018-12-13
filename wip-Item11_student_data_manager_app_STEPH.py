     # Item 11 -- Student Data Manager App (COMBINED)






#  Item 14
def get_non_empty_input(question):
    """ This function checks for non empty input and prompts
    the user to enter a non empty data """

    value = input(question)
    value = value.strip()
    while value == "":
        print("No value entered. Please enter a value.")
        value = input(question)
        value = value.strip()
    return value


#  Item 13          sjb alsmost fixed
def write_from_dictionary_to_file(d, filename):
    """ This method writes comma separated values from dictionary to file"""
    """
    This check should live in write to dict function
    Check three things before over-writing to file:
        if file has header and atleast one student so two lines in file,
            add those two lines, incliding header in dict 

        if file empty?    (maybe change code in write to dict funciton)
            grab header line in dict eg. key == string ID, copy first to file
            then append the rest of the the dict to file. (write append feature function?)

        if file has header line from when it was generated ONLY
            append the rest of the dict or write header in dict 


         NOTE: we need two kinds of write to file modes one for append and one for over-write
         
                if option append mode, seek() the end of the file to append   

    """

    print("=============================================")
    print("dictionary object: ", d)
    print("file name: ", filename)
    print("=============================================")

    #open the file in write mode
    f = open(filename,'a')

    #f.seek(2)

    ####### if key == "id"
            #  f.    

    #if the id (key) exists in the dictionary, write the key and values in the file
    for key in d:
        #if f.read(2) == '\n\n':  
        file_value_part = d[key]            
        print("++++++++++++++++++++++++++++++++++++++++++++++")
        
    

        f.write(key + "," + file_value_part["Student Name"] + "," + str(file_value_part["Final Marks"]) + "," + file_value_part["Final Grade"] + "\n")

        print("++++++++++++++++++++++++++++++++++++++++++++++")
    
    f.close()



#  Item 12            sjb                   ########################################################################
def load_csv_file_to_dictionary(fname):
    """
    This check should live in write to dict function
    Check three things before over-writing to file:
        if file has header and atleast one student so two lines in file,
            add those two lines, incliding header in dict 

        if file empty?    (maybe change code in write to dict funciton)
            grab header line in dict eg. key == string ID, copy first to file
            then append the rest of the the dict to file. (write append feature function?)

        if file has header line from when it was generated ONLY
            append the rest of the dict or write header in dict 


         NOTE: we need two kinds of write to file modes one for append and one for over-write
         
                if option append mode, seek() the end of the file to append   

    """
    student_id_data = {}


    print(student_id_data)


    f = open(fname, "r")
    lines = f.readlines()
    f.close()
    data_lines = lines[1:]
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("data_lines: ", data_lines)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    for line in data_lines:
        line = line.strip()
        words = line.split(",")
        student_names = words[1]           # changed from [0] to [1]
        student_id = words[0]              # chaned from words[1] to [0]
   
        print("student_id: ", student_id)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        final_marks = float(words[2])
        final_grade = words[3]
        student_id_data[student_id] = {}
        student_id_data[student_id]["Student Name"] = student_names
        student_id_data[student_id]["Final Marks"] = final_marks
        student_id_data[student_id]["Final Grade"] = final_grade

    print("Test load_csv_file_ditionary: ",student_id_data)

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


#  Item 1     ######## SJB CALL write to dictionary here after file data has been entered
def create_new_file(file_name):
    """
    This function takes a name for a file and creates a new student data file
    with comma separated 4 columns, and with its 1st row as the header for
    Student Name, ID, Marks and Letter Grade. User may enter student data in
    this new file before closing or quit to close the new file.
    """

    new_file = open(file_name, "w")
    print("\nYou have created a new file named: " + file_name + "\n")
    # write the 1st row which is the Header in 4 columns
    new_file.write("Student_Name,ID,Marks,Grade\n")
    entry = int(input("Do you want to enter data? (enter: 1 for Yes, 0 to Exit): \n"))

    while entry != 0:
        student_name = input("Enter Student Name: \n")
        id = input("Enter Student ID: \n")
        marks = input("Enter Student Marks: \n")
        grade = calculate_letter_grade(float(marks))
        new_file.write(student_name + "," + id + "," + marks + "," + grade + "\n")
        print("You entered: Student Name: " + student_name + ", Student ID: " + id +
              ", Student Marks: " + marks + ", Letter Grade: " + grade + "\n")
        entry = int(input("Do you want to enter another data? (enter: 1 for Yes, 0 to Exit): "))
    new_file.close()


    ##### call write() to dic here


# Item 2
def update_file(file_to_update):

    dictionary_file = load_csv_file_to_dictionary(file_to_update)
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("load_csv_file_to_dictionary:",dictionary_file)
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&")

    print("Enter 1 - to add a New Student\n" +
          "Enter 2 - to modify a student Name\n" +
          "Enter 3 - to modify a student Mark\n" +
          "Enter 4 - to remove a Student\n" +
          "Enter 0 - to exit\n")
    choice = int(get_non_empty_input("Enter a selection: \n"))
    print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{")
    print("user choice: ", choice)
    print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{")

    while choice != 0:
        if choice == 1:
            new_student_name = get_non_empty_input("Enter New Student Name: \n")
            #print("new_student_name: ", new_student_name)  #
            id = get_non_empty_input("Enter Student ID: \n")
            #print("student ID: ", id)  #
            marks = get_non_empty_input("Enter Student Marks: \n")
            #print("student marks: ", marks)   #
            grade = calculate_letter_grade(float(marks))
            print("Student grade: ", grade)   #

            dictionary_file[id] = {} 
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("dictionary_file: ", dictionary_file) #

            dictionary_file[id]["Student Name"] = new_student_name
            dictionary_file[id]["Final Marks"] = marks
            dictionary_file[id]["Final Grade"] = grade
            print("dict object final grade: ", grade)

            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            write_from_dictionary_to_file(dictionary_file,file_to_update)

            print("update_file dictionary: ", dictionary_file, "##############") 

        elif choice == 2:
            key_id = get_non_empty_input("Enter the Student ID: \n")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("key_id", key_id)
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if key_id in dictionary_file:
                dictionary_file[key_id]["Student Name"] = get_non_empty_input("Enter the new student name: \n")       ###
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("dict file object key: ", dictionary_file[key_id]["Student Name"])
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                write_from_dictionary_to_file(dictionary_file, file_to_update)

        elif choice == 3:
            key_id = get_non_empty_input("Enter the Student ID: \n")
            if key_id in dictionary_file:
                dictionary_file[key_id]["Final Marks"] = get_non_empty_input("Enter the new marks: \n")
                write_from_dictionary_to_file(dictionary_file, file_to_update)

        elif choice == 4:
            key_id = get_non_empty_input("Enter the Student ID: \n")
            remove_a_student(file_to_update, key_id)


# Item 3
def remove_a_student(remove_from_file, remove_id):
    dictionary_file = load_csv_file_to_dictionary(remove_from_file)

    if remove_id in dictionary_file:
        key_id = dictionary_file[remove_id]
        name = dictionary_file[remove_id]["Student Name"]
        del dictionary_file[remove_id]
        write_from_dictionary_to_file(dictionary_file, remove_from_file)
        print("Student: " + key_id + ", " + name + " is removed from file: "+ remove_from_file)
    else:
        print("Id " + remove_id + "not found.")



# Item 4
def search_student(search_in_file, student_lookup):
    pass

# Item 5
def file_summary(file_to_summarize):
    pass

# Item 6
def print_all(file_to_print):
    pass


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
        print("$$$$$$$$$$$$$$$$$$$$$$$$")
        print("\nInvalid selection.\n")
        print("$$$$$$$$$$$$$$$$$$$$$$$$")
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
            print("#################################################################################")
            print("this is the file to update: ", file_to_update)
            print(update_file(file_to_update), "##################") 
            print("#################################################################################")                                     ########

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
    return 3  # valid selection and entry = 1 to 6         ###### why are we entering 3 here instead pf calling the function again


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
              "*        5      -     Print only a summery of student data                *\n" +
              "*        6      -     Print the entire student data file to command line  *\n" +
              "*        0      -     Quit                                                *\n" +
              "***************************************************************************\n")
        print("Welcome to Student Database System!")
        read_entry = input("Enter a selection from the menu (Or 0 to quit): ")
        if student_data_manager(read_entry) == 2:
            break


main()