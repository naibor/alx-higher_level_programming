#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C

    Args:
        my_string: the string

    Returns:
        returns a new string
    """
    my_string = my_string.replace('c', "")
    my_string = my_string.replace('C', "")
    return my_string
