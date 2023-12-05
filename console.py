#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter."""

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True