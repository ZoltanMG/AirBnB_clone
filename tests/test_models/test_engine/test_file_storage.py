"""
Module of test FileStorage
"""


import unittest


class TestFileStorage(unittest.TestCase):
    '''
    Test cases for file_storage class
    '''

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
