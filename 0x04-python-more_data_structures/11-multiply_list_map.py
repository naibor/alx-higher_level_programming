#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """ multiply values of by a number
    Args:
        my_list: the list
        number: the number to multiply it by
    Returns:
        returns a list
    """
    new_list = [x * number for x in my_list]
    return new_list
