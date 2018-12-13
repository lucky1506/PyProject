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
