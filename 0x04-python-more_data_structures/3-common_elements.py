#!/usr/bin/python3
def common_elements(set_1, set_2):
    """ gets common elements
    Args:
        set_1: first set
        set_2: second set
    Returns:
        returns a set
    """
    new_set = set_1 & set_2
    return new_set
