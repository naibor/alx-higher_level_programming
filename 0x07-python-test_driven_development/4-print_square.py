#!/usr/bin/python3
"""
Module print_square
Itt  prints out a square using #
"""


def print_square(size):
    """ Prints a square
    Args:
        size: the size of the square
    Raise:
        TypeError if size is not an int
        ValueError if size is <= 0
    """
    # handle exceptions
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    # print square
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
