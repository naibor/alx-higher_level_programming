#!/usr/bin/python3

class Square:
    """ A Square
    Attributes:
        size: type int
    """
    def __init__(self, size=0):
        """ Intitilize class square with attribute size
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Calculate the area of a square
        """
        return self.__size ** 2
