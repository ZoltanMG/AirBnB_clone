#!/usr/bin/env python3
'''
'''


import json


class FileStorage:
    '''
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):

        if obj is not None:
            keys = obj.__class__.__name__ + '.' + obj.id
            to_dict = obj.to_dict()
            self.__objects[keys] = to_dict

    def save(self):
        with open(self.__file_path, 'w', encoding="utf-8") as files:
            abc = json.dumps(self.__objects)
            files.write(abc)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as files:
                self.__objects = json.load(files)
        except:
            pass
