#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter."""

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass