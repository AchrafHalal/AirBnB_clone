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

   