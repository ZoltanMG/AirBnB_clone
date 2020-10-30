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
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                    print("kwargs", type(self.created_at))
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'name':
                    self.name = value
                elif key == 'my_number':
                    self.my_number = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            print("Hola ", type(self.created_at))
            self.updated_at = datetime.now()
            print(self.to_dict())
            storage.new(self)


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
        storage.save()

    def to_dict(self):
        """
        in this method a dictionary is returned with the attributes of
        the classes and the name of the class.
        """
        my_dict = self.__dict__
        print("Hola1 ", type(my_dict['created_at']))
        my_dict['created_at'] = self.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        my_dict['updated_at'] = self.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
