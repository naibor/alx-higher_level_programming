#!/usr/bin/python3
"""Defining a class Square."""


class Square:
    """ A Square
    Attributes:
        size (int): private attribute
    """
    def __init__(self, size=0):
        """ Intitilize class square with attribute size
        Args:
            size (int): parameter
        """
        self.__size = size

    @property
    def size(self):
        """ Retrieves the attribute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the attribute size
        Args:
            value (int): New value for size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculate the area of a square
        """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square
        """
        # get the size
        the_size = self.__size
        # check if the size is == 0
        if the_size == 0:
            print()
        else:
            for length in range(the_size):
                for width in range(the_size - 1):
                    print("#", end="")
                print("#")
