#!/usr/bin/python3

"""Defining a class rectangle. """


class Rectangle:
    """ A rectangle
    Attributes:
        width(int): private attribute
        height(int): private attribute
    """
    def __init__(self, width=0, height=0):
        """ Initilizr class with attributes
        Args:
            width(int): the width of rectangle
            height(int): the height of rectangle
        """
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Returns an informal printable string repr
        of rectangle with '#'
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        the_print = ''
        for i in range(self.__height):
            for j in range(self.__width):
                the_print += '#'
            the_print += '\n'
        return the_print[:-1]

    @property
    def width(self):
        """ Getter method for width
        Returns:
            returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method, sets value of width
        Args:
            value(int): the value to set
        Returns:
            Returns the value
        """
        # check if value is int
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method for height
        Returns:
            returns height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for value of height
        Args:
            value(int): the value to set
        Returns:
            returns the set value
        """
        # check if value is int
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates the area of rectangle
        Returns:
            returns the product of weigth and height
        """
        return self.__height * self.__width

    def perimeter(self):
        """ Calculates perimeter of a rectangle
        Returns:
            returns the perimeter
        """
        # check if either width or height is 0 and return 0
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            perimeter = (self.__width * 2) + (self.__height * 2)
        return perimeter
