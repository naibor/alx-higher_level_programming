#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the items at an index

    Args:
        my_list: the list
        idx: the index to delete
    Returns:
        the same list if idx is out of range or -ve
    """
    # get length of list
    length = len(my_list)

    if idx < 0:
        return my_list
    elif idx >= length:
        return my_list
    else:
        del my_list[idx]
    return my_list
