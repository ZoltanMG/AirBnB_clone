#!/usr/bin/python3
"""
Module of test FileStorage
"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''
    Test cases for file_storage class
    '''

    def test_checking_for_docstring_FileStorage(self):
        """checking for docstrings"""

        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.delete.__doc__)

    def setUp(self):
        '''
        simple set up
        '''
        self.my_model = BaseModel()
        self.storage = FileStorage()

    def test_new(self):
        '''
        tests new method in file storage
        '''
        self.storage.new(self.my_model)
        new_dict = self.storage.all()
        key = self.my_model.__class__.__name__ + '.' + self.my_model.id
        self.assertIsInstance(new_dict[key], BaseModel)

    def test_all(self):
        '''
        tests if all returns a dict
        '''
        self.assertIsInstance(self.storage.all(), dict)

if __name__ == "__main__":
    unittest.main()
