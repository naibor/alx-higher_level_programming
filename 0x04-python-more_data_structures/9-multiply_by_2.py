#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """ multiply values in a dict by 2
    Args:
        a_dictionary: the said dictionary
    Returns:
        return a new dictionary
    """
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
