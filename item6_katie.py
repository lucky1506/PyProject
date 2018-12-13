

def print_all(file_to_print):
    with open(file_to_print) as fileref:
        fileref.readline() # skip header of txt file
        print('_'*60)
        print('')
        header = 'STUDENT NAME,ID,MARKS,GRADE'
        name, idn, marks, grade = header.split(',')
        print(f'{name:<30}{idn:^10}{marks:^10}{grade:^10}')
        print('_'*60)
        print('')
        for line in fileref:
            name, idn, marks, grade = line.split(',')

            print(f'{name:<30}{idn:^10}{marks:^10}{grade:^10}')
    # display first 20 records
    # then ask to display next 20 records