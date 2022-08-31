#!/usr/bin/python3
def weight_average(my_list=[]):
    """ gets the weighted average
    Args:
        my_list: the list to work on
    Returns:
        returns average
    """
    sum_of = 0
    divide_by = 0
    if len(my_list) == 0:
        return 0
    for item in my_list:
        sum_of = sum_of + (item[0] * item[1])
        divide_by = divide_by + item[1]
    return sum_of/divide_by
