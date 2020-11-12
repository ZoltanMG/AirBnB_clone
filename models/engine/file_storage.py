#!/usr/bin/python3
"""
This module allows you to create, save and load dictionaries
based on previouslycreated objects, all this is generated
through JOSN serialization and deserialization.
"""


import json
from datetime import datetime


class FileStorage:
    """
    This class allows you to create an object that interacts with the created
    instances and with the file.JSON file as follows:

    Attributes:
    __file_path: contains the path / name of the file.
    __objects: It is an initially empty dictionary where elements will be
    added, updated or deleted based on the objects created.

    Methods:

    all: returns __objects
    new: adds an item to the __objects dictionary.
    save: saves the updated or modified dictionary to the file specified in the
    __file_path variable.
    reload: load __objects the file information from the __file_path variable.
    remove - removes an item from the __objects dictionary.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary with the data of
        previously created or modified instances.
        """

        return self.__objects

    def new(self, obj):
        """
        Add a new element to the __objects dictionary
        """

        if obj is not None:
            keys = obj.__class__.__name__ + '.' + obj.id
            self.__objects[keys] = obj

    def save(self):
        """
        Stores the dictionary of __objects in JSON format
        in a file specified in the variable __file_path.
        """

        new_object = {}

        with open(self.__file_path, 'w', encoding="utf-8") as files:
            new_dict = self.__objects.copy()
            for key, value in new_dict.items():
                new_object[key] = value.to_dict()
            abc = json.dumps(new_object)
            files.write(abc)

    def reload(self):
        """
        It extracts the information in JSON format from the file specified in
        the __file_path variable and transforms it into a dictionary
        to be stored in the __objects variable.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        try:
            with open(self.__file_path, 'r', encoding="utf-8") as files:
                self.__objects = json.load(files)

                for key, value in self.__objects.items():
                    self.new(eval(value['__class__'])(**value))
        except:
            pass

    def delete(self, key):
        """
        Removes an element from the __objects variable and saves the changes to
        the file specified in __file_path.
        """

        del self.__objects[key]
        self.save()
