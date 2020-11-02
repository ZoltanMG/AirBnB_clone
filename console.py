#!/usr/bin/env python3
"""AirBnB Console"""

import cmd
from models.user import User

class HBNBCommand(cmd.Cmd):
    """ Class HBNB to read command """
    prompt = '(hbnb)'

    def do_quit(self, args):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def emptyline(self):
        """Pass if no command is given"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
