# Item 12

def load_csv_file_to_dictionary(fname):
    student_id_data = {}

    f = open(fname, "r")
    lines = f.readlines()
    f.close()
    data_lines = lines[1:]

    for line in data_lines:
        line = line.strip()
        words = line.split(",")
        student_names = words[0]
        student_id = words[1]
        final_marks = float(words[2])
        final_grade = words[3]
        student_id_data[student_id] = {}
        student_id_data[student_id]["Student Name"] = student_names
        student_id_data[student_id]["Final Marks"] = final_marks
        student_id_data[student_id]["Final Grade"] = final_grade


    return student_id_data
