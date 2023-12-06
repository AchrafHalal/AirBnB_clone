#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

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

    def default(self, arg):
        """Default cmd when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argu = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argu[1])
            if match is not None:
                command = [argu[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argu[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
    
    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True
    
    def do_create(self, arg):
        """Create a new class instance and print its id."""

        argu = parse_argu(arg)
        if len(argu) == 0:
            print("** class name missing **")
        elif argu[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argu[0])().id)
            storage.save()
    
    def do_show(self, arg):
        """Show the string representation of a class instance based on the class name and id."""
        argu = parse_argu(arg)
        object = storage.all()
        if len(argu) == 0:
            print("** class name missing **")
        elif argu[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argu) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argu[0], argu[1]) not in object:
            print("** no instance found **")
        else:
            print(object["{}.{}".format(argu[0], argu[1])])

    def do_destroy(self, arg):
        """Delete a class instance of an id."""
        argu = parse_argu(arg)
        object = storage.all()
        if len(argu) == 0:
            print("** class name missing **")
        elif argu[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argu) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argu[0], argu[1]) not in object.keys():
            print("** no instance found **")
        else:
            del object["{}.{}".format(argu[0], argu[1])]
            storage.save()   

    def do_all(self, arg):
        """All the instance to be shown"""

        argu = parse_argu(arg)
        if len(argu) > 0 and argu[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argu) > 0 and argu[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argu) == 0:
                    objl.append(obj.__str__())
            print(objl)  

    def do_count(self, arg):
        """count the number of instances of a  class.""" 
        argu = parse_argu(arg)
        count = 0
        for obj in storage.all().values():
            if argu[0] == obj.__class__.__name__:
                count += 1
        print(count)         

    def do_update(self, arg):
        """Update the instances."""
        argu = parse_argu(arg)
        object = storage.all()

        if len(argu) == 0:
            print("** class name missing **")
            return False
        if argu[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argu) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argu[0], argu[1]) not in object.keys():
            print("** no instance found **")
            return False
        if len(argu) == 2:
            print("** attribute name missing **")
            return False
        if len(argu) == 3:
            try:
                type(eval(argu[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(argu) == 4:
            obj = object["{}.{}".format(argu[0], argu[1])]
            if argu[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argu[2]])
                obj.__dict__[argu[2]] = valtype(argu[3])
            else:
                obj.__dict__[argu[2]] = argu[3]
        elif type(eval(argu[2])) == dict:
            obj = object["{}.{}".format(argu[0], argu[1])]
            for k, v in eval(argu[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()                  

if __name__ == '__main__':
    HBNBCommand().cmdloop()    