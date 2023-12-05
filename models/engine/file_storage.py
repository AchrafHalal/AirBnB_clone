#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel



class FileStorage:
    """Storage classe for processing and storing data."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects
    
    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {}
        for obj in odict.keys():
            objdict[obj] = odict[obj].to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)
    



   