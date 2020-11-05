#!/usr/bin/python3
"""
This is a module to test.
"""


import unittest
from datetime import datetime
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """
    Test the amenity model class
    """

    def setUp(self):
        self.models = Amenity()
        self.models.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.models, "name"))
        self.assertEqual(self.models.name, "")


if __name__ == "__main__":
    unittest.main()
