#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """ get all different elements
    Args:
        set_1: first set
        set_2: second set
    Returns:
        a set
    """
    new_set = set_1 ^ set_2
    return new_set
