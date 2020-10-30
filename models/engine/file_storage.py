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
        return __class__.__objects

    def new(self, obj):

       keys = obj["__class__"] + '.' + obj["id"]
       __class__.__objects[keys]=obj

    def save(self):
        print("Hola paso por aqui")
        with open(self.__file_path,'w', encoding = "utf-8") as files:
            json_str=json.dumps(__class__.__objects)
            files.write(json_str)
    def reload(self):
        pass
