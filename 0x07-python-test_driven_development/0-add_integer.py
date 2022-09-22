#!/usr/bin/python3

def add_integer(a, b=98):
    """ Add two integers
    Args:
        a(int): first value
        b(int): second value
    Raises:
        TypeError: Exception raised when value is not of type int
    Returns:
        returns sum of integers
    """
    # check value a is int
    if type(a) != int:
        if type(a) == float:
            # type cast if of type float
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    # check value b is int
    if type(b) != int:
        # check if float and type cast
        if type(b) == float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
