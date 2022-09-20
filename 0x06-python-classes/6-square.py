#!/usr/bin/python3
"""Defining a class Square."""


class Square:
    """ A Square
    Attributes:
        size: type int
        position: type tuple with int
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Intitilize class square with attribute size and position
        Args:
            size (int): size parameter
            position(tuple): position parameter of type int
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Retrieves the attribute size
        """
        return self.__size

    @property
    def position(self):
        """ Retrieve the attribute position
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """ Set the attribute position
        Args:
            value (tuple): New value for position
        """
        # get length
        m = len(value)

        # check for value error
        if not isinstance(value, tuple) or m != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculate the area of a square
        """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square
        """
        # get the size and position
        the_size = self.__size
        the_position = self.__position

        # check if the size is == 0
        if the_size == 0:
            print()
        else:
            for x in range(the_position[1]):
                print()
            for length in range(the_size):
                for item in range(the_position[0]):
                    print(" ", end="")
                for width in range(the_size - 1):
                    print("#", end="")
                print("#")
