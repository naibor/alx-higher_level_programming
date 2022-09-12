#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ Prints a list of integers

    Args:
        my_list: list to be printed
        x: number of elementsto print
    Returns:
        returns number of ints printed
    """
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
