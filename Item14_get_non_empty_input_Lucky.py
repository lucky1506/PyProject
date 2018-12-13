#  Item 14
def get_non_empty_input(question):
    """ This function checks for non empty input and prompts
    the user to enter a data """
    value = input(question)
    value = value.strip()
    while value == "":
        print("No value entered. Please enter a value.")
        value = input(question)
        value = value.strip()
    return value