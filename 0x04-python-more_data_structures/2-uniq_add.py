#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ adds all unique integers
    Args:
        my_list: list to work on
    Return:
        returns sum
    """
    new_list = set(my_list)
    sum_of = 0
    for item in new_list:
        sum_of = sum_of + item
    return sum_of
