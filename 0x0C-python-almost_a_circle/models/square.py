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

    @property
    def size(self):
        """getter method for size value
        Return:
            Private value size value
        """
        return self.width

    @size.setter
    def size(self, value):
        """setter method for size value
        Args:
            value (int): value to check if is int and gratter than 0
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.width = value

    def update(self, *args, **kwargs):
        """Updates Square class
        Args:
            args (list): arguments to update rectangle class
            kwargs (dict): arguments to update rectangle class
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Creates a dictionary representation for Square
        Return:
            A dictionary representation
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
