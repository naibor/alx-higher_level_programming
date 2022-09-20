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
