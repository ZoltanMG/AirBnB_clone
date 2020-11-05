#!/usr/bin/python3

"""
Review Test
"""


import unittest
from models.review import Review
from models.base_model import BaseModel


class reviewTest(unittest.TestCase):
    """
    Test reviewTest class
    """

    def setUp(self):
        self.model = Review()
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "place_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "text"))
        self.assertEqual(self.model.place_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.text, "")

if __name__ == "__main__":
    unittest.main()
