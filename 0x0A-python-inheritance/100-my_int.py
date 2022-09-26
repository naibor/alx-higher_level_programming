#!/usr/bin/python3
"""
Module: 100-my_int
Inherits int and modify functionality
"""


class MyInt(int):
    """MyInt class
    """
    def __eq__(self, num):
        """
        == function
        Attributes:
            num (int): an input
        Returns:
            The != boolean of input
        """
        return (int(self) != num)

    def __ne__(self, num):
        """
        != function
        Attributes:
            num (int): an input
        Returns:
            The == boolean of input
        """
        return (int(self) == num)
