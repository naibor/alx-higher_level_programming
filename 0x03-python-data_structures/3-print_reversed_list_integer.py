#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints a list in reverse

    Args:
        my_list: the list to work on

    """

    # length of my_list
    length = len(my_list) - 1

    while length >= 0:
        print("{}".format(my_list[length]))
        length = length - 1
