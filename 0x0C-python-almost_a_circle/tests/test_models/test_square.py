#!/usr/bin/python3
""" Unittest square
Test cases for class Square
"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    """ Test class for square class"""

    def setUp(self):
        Base._Base__nb_objects = 0
    
    # Task 10
    def test_010_0(self):
        """Test Square class: test attributes."""

        s0 = Square(1)
        self.assertEqual(s0.id, 1)
        s1 = Square(5, 3, 4)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 2)
