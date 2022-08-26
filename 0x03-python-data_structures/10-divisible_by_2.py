#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Multiples of 2

    Args:
        my_list: the list to look through
    Returns:
        returns a new list with Trues or False
    """
    new_list = []
    for item in my_list:
        if item % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
