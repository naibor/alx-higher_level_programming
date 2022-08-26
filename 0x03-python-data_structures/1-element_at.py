#!/usr/bin/python3
def element_at(my_list, idx):
    """ My element at

    Args:
        my_list: the list to work on
        idx: the position of item

    Returns:
        returns None if idx is -ve or out of range
    """
    # get length of list
    length = len(my_list)

    if idx < 0:
        return None
    elif idx >= length:
        return None
    else:
        return my_list.pop(idx)
