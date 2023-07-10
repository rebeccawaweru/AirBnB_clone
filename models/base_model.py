#!/usr/bin/python3
"""Define BaseModel class"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Representing the BaseModel of the project"""
    def __init__(self):
        """Initialize new BaseModel instance"""
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """Updating updated_at with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        newdict = self.__dict__.copy()
        newdict["created_at"] = self.created_at.isoformat()
        newdict["updated_at"] = self.updated_at.isoformat()
        newdict["__class__"] = self.__class__.__name__
        return newdict

    def __str__(self):
        """Returns the string representation of the class BaseModel"""
        cls = self.__class__.__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)
