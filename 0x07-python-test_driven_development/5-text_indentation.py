#!/usr/bin/python3
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
