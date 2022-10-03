#!/usr/bin/python3
""" Unittest rectangle
Test cases for class Rectangle
"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """ Test cases for rectangle class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_2_001(selfi):
        """ Test for id"""

         r1 = Rectangle(10, 2)
         self.assertEqual(r1.id, 1)
         r2 = Rectangle(2, 10)
         self.assertEqual(r2.id, 2)
         r3 = Rectangle(10, 2, 0, 0, 12)
         self.assertEqual(r3.id, 3)

    def test_2_002(self):
        """ Test for attribute values"""

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r3 = Rectangle(10, 2, 4, 5, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)
