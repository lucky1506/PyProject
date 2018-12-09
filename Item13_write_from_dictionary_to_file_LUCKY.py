# Item 13

def write_from_dictionary_to_file(d, filename):
    """ This method writes comma separated values from dictionary to file"""

    # open the file in write mode
    f = open(filename, "w")

    # if the id (key) exists in the dictionary, write the key and values in the file
    for key in d:
        value_list = d[key]
        f.write(key + "," + value_list[0] + "," + value_list[1] + "," + value_list[2] + "\n")
    f.close()
