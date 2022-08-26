#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """My replace function

    Args:
        my_list: the list to work on
        idx: the idex of the element
        element: the element to replace with

    Returns: 
        the original list if idx is -ve or out of range
    """
    # get length of list
    length = len(my_list)

    if idx < 0:
        return my_list
    elif idx >= length:
        return my_list
    else:
        my_list[idx] = element
        return my_list
