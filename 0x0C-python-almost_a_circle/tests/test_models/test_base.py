#!/usr/bin/python3
""" Unittest base
Test cases for Base class
"""


import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test class Base """

    def setUp(self):
        """ Test class setup"""
        Base._Base__nb_objects = 0

    def test_001(self):
        """ Creating a new instance of Base class. Check attribute id """
        
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 5)
        b6 = Base(-6)
        self.assertEqual(b6.id, -6)

    def test_002(self):
        """ Test the type and instance"""
        
        # create an instance
        b7 = Base()
        self.assertEqual(type(b7), Base)
        self.assertTrue(isinstance(b7, Base))


