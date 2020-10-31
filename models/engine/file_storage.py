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
            self.__objects[keys] = obj

    def save(self):
        new_object = {}
        with open(self.__file_path, 'w', encoding="utf-8") as files:
            for key in self.__objects:
                new_object[key] = self.__objects[key].to_dict()
            abc = json.dumps(new_object)
            files.write(abc)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as files:
                self.__objects = json.load(files)
                value = self.__objects['created_at']
                self.__objects['created_at'] = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                value = self.__objects['created_at']
                self.__objects['created_at'] = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
            for key in self.__object:
                print(self.__object[key])
        except:
            pass
