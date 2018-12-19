

def print_all(file_to_print):
    """ Print entire file row-by-row. User chooses to display 20 records at a time or print the entire file."""
    with open(file_to_print) as student_records:
        student_records.readline() # skip header of txt file
        print('_'*60)
        print('')
        header = 'STUDENT NAME,ID,MARKS,GRADE'
        name, idn, marks, grade = header.split(',')
        print(f'{name:<30}{idn:^10}{marks:^10}{grade:^10}')
        print('_'*60)
        print('')
        line_count = 0 # will keep track of how many records have been printed
        
        for line in file_to_print:      # print each record
            name, idn, marks, grade = line.split(',')
            print(f'{name:<30}{idn:^10}{marks:^10}{grade:^10}')
            line_count += 1
            if line_count % 20 == 0:   # only show 20 records at a time
                prompt_more = 'x'
                while prompt_more not in 'YyNn': # Make sure yes or no answer
                    prompt_more = input('Would you like to see the next 20 records? Enter Y or N.  ')
                if prompt_more in 'Yy':
                    continue
                else:
                    break

