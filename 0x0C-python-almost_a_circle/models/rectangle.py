#!/usr/bin/python3
"""
Module: rectangle
Class Rectangle that inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class
    Private instance attribute:
        __width
        __height
        __x
        __y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize class rectangle
        Args:
            width(int)
            height(int)
            x(int)
            y(int)
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for width
        Args:
            value: the value to set
        """

        self.__width = value

    @property
    def height(self):
        """ getter method for height """
        return self.__width

    @height.setter
    def height(self, value):
        """ Setter method for height
        Args:
            value: the value to set
        """

        self.__height = value

    @property
    def x(self):
        """ getter method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter method for x
        Args:
            value: the value to set
        """

        self.__x = value

    @property
    def y(self):
        """ getter method for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter method for y
        Args:
            value: the value to set
        """

        self.__y = value
