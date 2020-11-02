import unittest
from models.base_model import BaseModel
from datetime import datetime

class Test_BaseModel(unittest.TestCase):
    """ Test the base model class """

    def test_types(self):
        """ Type of argument """
        base = BaseModel()
        self.assertEqual(type(base.id), str)
        self.assertEqual(type(base.created_at), datetime)
        self.assertEqual(type(base.updated_at), datetime)

if __name__ == "__main__":
    unittest.main()
