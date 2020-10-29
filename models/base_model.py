#!/usr/bin/python3
"""
"""


import uuid
from datetime import datetime


class BaseModel:
    """
    """

    def __init__(self):
        """
        """

        self.id = str(uuid.uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """
        """

        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """
        """

        self.update_at = datetime.now()

    def to_dict(self):
        """
        """

        self.create_at = self.create_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.update_at = self.update_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
