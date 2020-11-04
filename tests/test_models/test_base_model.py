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

    def setUp(self):
        """ """
        self.base = BaseModel()

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

        basemodel_dict = self.base.to_dict()
        self.assertEqual(str(type(basemodel_dict)), "<class 'dict'>")
        self.assertEqual(type(self.base.id), str)
        self.assertEqual(type(self.base.created_at), datetime)
        self.assertEqual(type(self.base.updated_at), datetime)

    def test_instantiaton(self):
        """ Arguments in Kwarg """

        d = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
             'created_at': '2017-09-28T21:03:54.053212',
             '__class__': 'BaseModel',
             'updated_at': '2017-09-28T21:03:54.056732'}
        b1 = BaseModel(**d)
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "__class__"))
        self.assertTrue(b1.__class__ not in b1.__dict__)

    def test_save(self):
        '''
        tests created_at and updated_at values after call to save
        '''
        first_dict = self.base.to_dict()
        self.base.save()
        second_dict = self.base.to_dict()
        self.assertEqual(first_dict["created_at"], second_dict["created_at"])
        self.assertNotEqual(
            first_dict["updated_at"], second_dict["updated_at"])

    def test_args(self):
        '''
        tests args
        '''
        self.base.name = "Holberton"
        self.assertEqual(self.base.name, "Holberton")




if __name__ == "__main__":
    unittest.main()
