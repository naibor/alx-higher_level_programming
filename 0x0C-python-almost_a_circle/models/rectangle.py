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

    # validator method
    def validator(self, name, value):
        """ Validate the values
        Args:
            name: name of attribute
            values: what to validate
        """

        # check type and value errors
        # import pdb; pdb.set_trace()
        if type(value) is not int:
            raise TypeError("{} must be an integer". format(name))
        while name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0". format(name))
        while name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be > 0". format(name))

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
        width = self.validator("width", value)
        self.__width = width

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for height
        Args:
            value: the value to set
        """
        height = self.validator("height", value)
        self.__height = height

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
        x = self.validator("x", value)
        self.__x = x

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
        y = self.validator("y", value)
        self.__y = y

    def area(self):
        """
        Calculates the area
        Returns:
            The area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Prints a Rectangle using #
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """str repr method
        Return:
            The string: [class_name] (id) x/y - width/height
        """
        string = "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                  self.id, self.x, self.y,
                                                  self.width, self.height)
        return string

    def update(self, *args):
        """ Update, assigns a variable to each attribute
        Args:
            *args
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]