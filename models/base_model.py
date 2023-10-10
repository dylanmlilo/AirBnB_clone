#!/usr/bin/python3
""" Defines a base model package for AirBnB clone """

import uuid
from datetime import datetime


class BaseModel:
    """ Defines a base model class """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()
    
    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
    
    def save(self):
        self.updated_at = datetime.now().isoformat()
        

    def to_dict(self):
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = datetime.strptime(object_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        object_dict['updated_at'] = datetime.strptime(object_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        return object_dict
