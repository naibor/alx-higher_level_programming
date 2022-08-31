#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """ replace or add items to a dict
    Args:
        a_dictionary: the dictionary to work on
        key: the key
        value: the value
    Returns:
        returns a dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
