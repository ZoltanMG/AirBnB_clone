#!/usr/bin/env python3
'''
'''


import json
from datetime import datetime


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
            for key in self.__objects:
                print('NEW------>>>>',type(self.__objects[key]))

    def save(self):
        new_object = {}
        for key in self.__objects:
            print('SAVE------>>>>',type(self.__objects[key]))
        with open(self.__file_path, 'w', encoding="utf-8") as files:
            for key,value in self.__objects.items():
                print("Save-->",self.__objects[key])
                print("Save type-->", type(self.__objects[key]))
                new_object[key] = value.to_dict()
            abc = json.dumps(new_object)
            files.write(abc)

    def reload(self):
        try:
            print("self.__object Antes", self.__objects)
            print("TYPE RELOAD ANTES-->", type(self.__objects))
            with open(self.__file_path, 'r', encoding="utf-8") as files:
                self.__objects = json.load(files)

                for key, value in self.__objects.items():
                    print("Key--->", key)
                    #if  == 'created_at':
                    #ivalue = self.__objects[key]
                    #value = ivalue['created_at']
                    print("value-->", value)
                    time = value['created_at']
                    print("time-->", time)
                    new_time  = datetime.strptime(time,"%Y-%m-%dT%H:%M:%S.%f")
                    print("Hola-->\n")
                    value['created_at'] = new_time
                    #value = ivalue['update_at']
                    print("value2-->", value)
                    time = value['updated_at']
                    print("Antes updated-->")
                    new_time = datetime.strptime(time,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                    print("Despues updated-->")
                    value['updated_at'] = new_time
                    print("alleluya")
                    print(self.__objects[key])
                    print("TYPE RELOAD-->", type(self.__objects))
        except:
            pass
