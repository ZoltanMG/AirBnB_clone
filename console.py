#!/usr/bin/python3
"""
AirBnB Console
"""


import cmd
from models import storage
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Class HBNB to read command
    """

    prompt = '(hbnb) '

    def do_quit(self, args):
        """
        Quit command to exit the program
        """

        return True

    def do_EOF(self, args):
        """
        EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Pass if no command is given
        """

        pass

    def do_create(self, args):
        """
        create an instance of the class
        """

        commands = args.split()
        if len(commands) == 0:
            print('** class name missing **')
            return
        try:
            my_model = eval('{}()'.format(commands[0]))
            my_model.save()
            print(type(my_model))
            print(my_model.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        shows a specific item saved
        """

        commands = args.split()
        if len(commands) == 0:
            print('** class name missing **')
            return
        try:
            eval('{}()'.format(commands[0]))
            if len(commands) == 1:
                print("** instance id missing **")
                return
            inst_key = commands[0] + '.' + commands[1]
            objects = storage.all()
            print(objects[inst_key])
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        remove an item from the list
        """

        commands = args.split()
        if len(commands) == 0:
            print('** class name missing **')
            return
        try:
            eval('{}()'.format(commands[0]))
            if len(commands) == 1:
                print("** instance id missing **")
                return
            inst_key = commands[0] + '.' + commands[1]
            objects = storage.all()
            if objects[inst_key]:
                storage.delete(inst_key)
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """
        shows all saved instances
        """

        objects = storage.all()
        ls_obj = []
        commands = args.split()
        if len(commands) == 0:
            for key, value in objects.items():
                if type(value) is not dict:
                    ls_obj.append(str(value))
                else:
                    ls_obj.append("[{}] ({}) {}".format(value['__class__'],
                                                        value['id'],
                                                        str(value)))
            print(ls_obj)
            return
        try:
            eval('{}()'.format(commands[0]))
            for key, value in objects.items():
                name_cls = key.split('.')
                if commands[0] == name_cls[0]:
                    if type(value) is not dict:
                        ls_obj.append(str(value))
                    else:
                        ls_obj.append("[{}] ({}) {}".format(value['__class__'],
                                                            value['id'],
                                                            str(value)))
            print(ls_obj)
        except NameError as err:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        update an instance
        """

        objects = storage.all()
        arguments = []
        commands = args.split()
        if len(commands) == 0:
            print("** class name missing **")
            return
        try:
            eval('{}()'.format(commands[0]))
            if len(commands) == 1:
                print("** instance id missing **")
                return

            inst_key = inst_key = commands[0] + '.' + commands[1]
            if objects[inst_key]:
                if len(commands) == 2:
                    print("** attribute name missing **")
                    return
                if len(commands) == 3:
                    print("** value missing **")

                obj = objects[inst_key]
                if type(obj) is not dict:
                    obj.__dict__[commands[2]] = commands[3].replace('\"', '')
                    obj.save()
                else:
                    obj[commands[2]] = commands[3].replace('\"', '')
                    objects[inst_key] = obj
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print('** value missing **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
