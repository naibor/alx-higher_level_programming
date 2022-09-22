#!/usr/bin/python3
"""
Module test_indentation
It prints a text with 2 lines after a set of characters; .,?:
"""


def text_indentation(text):
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.
    Args:
        text: the text to print
    Raise:
        TypeError if text is not a string
    """
    # handle exceptions
    if type(text) is not str:
        raise TypeError("text must be a string")
    # print text with two new lines
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
