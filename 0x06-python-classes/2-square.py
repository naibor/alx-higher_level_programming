#!/usr/bin/python3
"""Defining a class Square."""


class Square:
    """ A class square
    Attributes:
        size: the size of the square
    """
    def __init__(self, size=0):
        """ Inititlize the class square
        Args:
            size: (int)private attribute
        Raises:
            TypeError: size must be int
            ValueError: size must be greate than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
