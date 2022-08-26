#!/usr/bin/python3
def max_integer(my_list=[]):
    """Biggest integer in list

    Args:
        my_list: the said list
    Returns:
        None if list is empty
        otherwise the biggest int
    """
    # get length og list
    length = len(my_list)
    biggest = 0
    if length == 0:
        return None
    else:
        for item in my_list:
            if item > biggest:
                biggest = item
    return biggest
