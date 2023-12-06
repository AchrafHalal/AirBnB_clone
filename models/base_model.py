#!/usr/bin/python3
"""the BaseModel class of the project."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ the Base Model of All the project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""

        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_form)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update Last time with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dict for the class name of the object."""
        ndict = self.__dict__.copy()
        ndict["created_at"] = self.created_at.isoformat()
        ndict["updated_at"] = self.updated_at.isoformat()
        ndict["__class__"] = self.__class__.__name__
        return ndict

    def __str__(self):
        """Return the str representation ."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
