#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ Replaces an element in a list

    Args:
        my_list: the list
        idx: the position to replace
        element: the new element

    Returns:
        returns original list if idx is -ve or out of range
    """
    # get length of list
    length = len(my_list)
    # create a copy of list
    copy = [item for item in my_list]

    if idx < 0:
        return my_list
    elif idx >= length:
        return my_list
    else:
        copy[idx] = element
        return copy
