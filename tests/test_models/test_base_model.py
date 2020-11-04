#!/usr/bin/python3
"""
This module performs the tests of
the base model module.
"""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    """
    In this class the methods to generate
    the tests are generated.
    """

    def test_checking_for_docstring_BaseModel(self):
        """checking for docstrings"""

        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_types(self):
        """
        This method validates the data
        types of the attributes.
        """

        base = BaseModel()
        self.assertEqual(type(base.id), str)
        self.assertEqual(type(base.created_at), datetime)
        self.assertEqual(type(base.updated_at), datetime)

if __name__ == "__main__":
    unittest.main()
