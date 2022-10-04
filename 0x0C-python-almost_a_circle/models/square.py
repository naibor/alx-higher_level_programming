#!/usr/bin/python3
"""
Module: square
Class square, inherits from Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Class  Square
        Args:
            size (int): The size of the square
            x(int): from class Rectangle
            y(int): from class Rectangle
            id: from base
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """__str__ method for class Square
        Return:
            The string: [class_name] (id) x/y - size
        """
        string = "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                               self.id, self.x, self.y,
                                               self.size)
        return string
