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

    @property
    def size(self):
        """ Retrieves the attribute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the attribute size
        Args:
            value: New value for size
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
