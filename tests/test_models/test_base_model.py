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
