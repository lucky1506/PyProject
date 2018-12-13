import statistics

# Lucky Pataky, Grace Durham, Stephanie Boyette, and Katie Jones


def read_csv_and_create_dic(fileobj):

    student_id_data = {}

    file = fileobj.readlines()
    remove_first_line = file[1:]

    for line in remove_first_line:
        line = line.strip()
        word = line.split(",")
        student_names = word[0]
        student_id = word[1]
        final_marks = float(word[2])
        final_grade = word[3]
        student_id_data[student_id] = {}
        student_id_data[student_id]["Student Name"] = student_names
        student_id_data[student_id]["Final Marks"] = final_marks
        student_id_data[student_id]["Final Grade"] = final_grade

    return student_id_data


def check_duplicates():
    pass


def create_new_student_data_file():
    pass


def update_an_existing_student_data_file():
    pass

#sjb see items3_remove_a_student.py for this block of code
def remove_a_student(student_dic):


# sjb
def search_a_student(student_dic):
    """ Allow user to search for a student, by entering a student ID, 
    through a collection of records in a given student roster/file."""

    student_id = input("To conduct a search, please enter in a student ID, eg. '1234': ")

    if student_id in student_dic:
        return student_dic[student_id]

    else:
        while True:
            print("So sorry. It looks like that student ID does not exist.")
            print("Please select from the following options:")
            print("1 - Continue your search")
            print("0 - Exit the search option and quit")

            option = int(input("Please choose one of the menu options: "))
    
            if option == 0:
                print("You have chosen to discontinue to search and to exit, bye bye!")
                break

            if option == 1:
                search_a_student(student_dic)


def print_only_summary_of_student_data(student_dic):

    the_number_of_students= len(student_dic.keys())
    print("The number of students:", the_number_of_students)

    

    final_marks_list = []
    final_grade_list =[]

    for key, value in student_dic.items():
        for k, v in value.items():
            if k == "Final Marks":
                final_marks_list.append(v)
            elif k == "Final Grade":
                final_grade_list.append(v)
    final_marks_sum = sum(final_marks_list)


    average_total_marks = final_marks_sum/the_number_of_students
    print("The average total marks:", average_total_marks)



    copy_of_final_marks_list = final_marks_list[:]
    copy_of_final_marks_list.sort()

    if(len(final_marks_list) % 2 ==0):
        print("The median total marks:", (copy_of_final_marks_list[(len(final_marks_list)-1)//2] + copy_of_final_marks_list[len(final_marks_list)//2])/2)

    else:
        print("The median total marks:", copy_of_final_marks_list[len(final_marks_list)//2])


    print("The standard deviation of the total marks:", statistics.stdev(final_marks_list))




    print("Highest marks:", max(copy_of_final_marks_list))

    print("Minimum marks:", min(copy_of_final_marks_list))


    print("Number of 'A's:", final_grade_list.count("A"))

    print("Number of 'B's:", final_grade_list.count("B"))

    print("Number of 'C's:", final_grade_list.count("C"))

    print("Number of 'D's:", final_grade_list.count("D"))

    print("Number of 'F's:", final_grade_list.count('F'))



def print_the_entire_student_data_from_command_line():
    pass



def calculate_letter_grade():
    pass



def write_to_file():
    pass



def student_data_manager(student_dic):


    while True:
        print("1 - Create new student data file.")
        print("2 - Update an existing student data file")
        print("3 - Remove a student")
        print("4 - Search a student")
        print("5 - Print only summary of student data")
        print("6 - Print the entire student data from command line")

        option = int(input("Please choose one of the menu options: 1,2,3,4,5,6, or 0 to quit\n"))

        if option == 0:
            print("You've selected the option to quit bye bye")
            break
        elif option == 1:
            create_new_student_data_file()
        elif option == 2:
            update_an_existing_student_data_file()
        elif option == 3:
            print("Student record you have removed: ", remove_a_student(student_dic))
        elif option == 4:
            print("Search result: ", search_a_student(student_dic))
        elif option == 5:
            print_only_summary_of_student_data(student_dic)
        elif option == 6:
            print_the_entire_student_data_from_command_line()
        else:
            print("Please select an option 0-6")



def main():

    with open("existing_student_data.csv", "r") as fileobj:
        student_dic = read_csv_and_create_dic(fileobj)


    student_data_manager(student_dic)


main()