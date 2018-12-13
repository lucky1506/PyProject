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
