#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ sorted dictionary
    Args:
        a_dictionary: the dictionary in question
    Returns:
        returns dict
    """
    list_key = sorted(list(a_dictionary))
    for item in list_key:
        print("{}: {}".format(item, a_dictionary[item]))
