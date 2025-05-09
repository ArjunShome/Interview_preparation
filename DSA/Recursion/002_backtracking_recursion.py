"""
Backtracking algorithm for Recirsion
"""

def display_ordered(number, actual_number):
    """
    Print he number 1 to N , using backtracking recursion
    Args:
        number (_type_): the number to print
        actual_number (_type_): the number to print to the extent.
    """
    if number < 1:
        return
    display_ordered(number-1, actual_number)
    print(number)


def display_reversed(number, actual_number):
    if number < 1 :
        return
    print(number)
    display_reversed(number - 1, actual_number)

if __name__ == "__main__":
    number = int(input("Please provide the number to print in order: "))
    # display_ordered(number, number)
    display_reversed(number, number)