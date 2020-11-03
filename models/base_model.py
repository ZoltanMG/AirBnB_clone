#!/usr/bin/python3
"""
this module contains the base class "BaseModel".

"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    this is the base class that will be inherited in the other classes.

    """

    def __init__(self, *args, **kwargs):
        """
        Initializing an instance of this class can be done in two ways:
        1. Enter the data by calling and assigning the instance attributes.
        2. Enter a dictionary with the data of a previously created instance.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'udpated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        This method returns a string in the following format:
        "[<class name>] (<self.id>) <self .__ dict __>".
        """

        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """
        in this method the date and time of
        modification of the class is updated.
        """

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        in this method a dictionary is returned with the attributes of
        the classes and the name of the class.
        """

        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
