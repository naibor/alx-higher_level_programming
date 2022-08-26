#!/usr/bin/python3
def multiple_returns(sentence):
    """Gets length of a string and 1st char

    Args:
        sentence: the sentence

    Returns:
        Returns the length and first character
    """
    # get length of string
    length = len(sentence)

    if length == 0:
        return (length, None)
    else:
        first_char = sentence[0]
        return (length, first_char)
