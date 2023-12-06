#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage

def parse_argu(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter."""


    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review",
    }
    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
    
    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True
    
    def do_create(self, arg):
        """Create a new class instance and print its id."""
        
        argul = parse_argu(arg)
        if len(argul) == 0:
            print("** class name missing **")
        elif argul[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argul[0])().id)
            storage.save()
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()    