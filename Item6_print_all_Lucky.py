# Item 6   Re-wrote to print 20 data per page
def print_all(file_to_print):
    student_dic = load_csv_file_to_dictionary(file_to_print)
    the_number_of_students = len(student_dic.keys())
    all_keys = student_dic.keys()
    numpages = int(the_number_of_students / 20)
    if the_number_of_students%20 != 0:
        numpages +=1

    print('_' * 70)
    print('')
    header = 'Line No,STUDENT NAME,ID,MARKS,GRADE'
    line_num, name, idn, marks, grade = header.split(',')
    print(f'{line_num:^10}{name:<30}{idn:^10}{marks:^10}{grade:^10}')
    print('_' * 70)
    print('')


    line_count = 1
    page = 1

    while True:
        line_count = 1
        for student_id in all_keys:
            if line_count <= 20*page and line_count>20*(page-1):
                name = student_dic[student_id]["Student Name"]
                marks = student_dic[student_id]["Final Marks"]
                grade = student_dic[student_id]["Final Grade"]
                print(f'{line_count:^10}{name:<30}{student_id:^10}{marks:^10}{grade:^10}')
            line_count += 1

        if page <numpages:
            choice = input("\nPrint next 20? (Type 1 for Yes, Or press enter to Exit): \n")
            if choice == "1":
                page = page + 1
            else:
                break
        else:
            break
