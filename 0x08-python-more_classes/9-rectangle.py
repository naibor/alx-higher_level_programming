#!/usr/bin/python3

"""Defining a class rectangle. """


class Rectangle:
    """ A rectangle
    Attributes:
       number_of_instances(int): public class attributei
       print_symbol(any type): public attribute
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initilizr class with attributes
        Args:
            width(int): the width of rectangle
            height(int): the height of rectangle
        """
        self.__width = width
        self.__height = height
        # increment the number of instance class attribute
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ Returns an informal printable string repr
        of rectangle with print symbol
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        the_print = ''
        for i in range(self.__height):
            for j in range(self.__width):
                the_print += str(self.print_symbol)
            the_print += '\n'
        return the_print[:-1]

    def __repr__(self):
        """ Returns a formal string representation of rectangle
        able to recreate a new instance using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Deletes a rectangle instance
        and prints a message
        """
        # decrament the number of instance class attribute
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle
        Args:
            rect_1(Rectangle): the first rectangle
            rect_2(Rectangle): the second rectangle
        """
        # check that they are instances of Rectangle
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance
        where width = height = size
        Args:
            cls(Rectangle): the class to create an instance of
            size(int): the length og the rectangle
        """
        return cls(size, size)
