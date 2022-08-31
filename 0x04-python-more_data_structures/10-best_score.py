#!/usr/bin/python3
def best_score(a_dictionary):
    """ gets the biggest integer
    Args:
        a_dictionary: the dict to work

    Returns:
        returns a key
    """
    temp = 0
    student = None
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > temp:
                temp = value
                student = key
    return student
