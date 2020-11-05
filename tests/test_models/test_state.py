#!/usr/bin/python3

"""
Test_state class Unitest
"""


import unittest
from models.state import State
from models.base_model import BaseModel


class Test_State(unittest.TestCase):
    """
    Test the state model class
    """

    def setUp(self):
        self.model = State()
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "")


if __name__ == "__main__":
    unittest.main()
