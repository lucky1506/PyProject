#  Item 13
def write_from_dictionary_to_file(d_file, filename):
    """ This method writes comma separated values from dictionary to file"""

    # open the file in write mode
    f = open(filename, "w")
    f.write("Student Name,ID,Marks,Grade\n")

    # if the id (key) exists in the dictionary, write the key and values in the file
    for key in d_file:
        value = d_file[key]
        f.write(value["Student Name"] + "," + key + "," + str(value["Final Marks"]) + "," + value["Final Grade"] + "\n")
    f.close()
