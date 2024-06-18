#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from Models.base_model import BaseModel
from Models.user import User
from Models.product import Product
from Models.review import Review
from Models.order import Order
from Models.market import Market

class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Return the dictionary of objects."""
        return FileStorage.__objects
    
    def new(self, obj):
        """Add a new object to the dictionary."""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
        
    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()} 
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objdict, f)
            
    def reload(self):
        """Deserialize the JSON file __file_path to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    cls_name = obj['__class__']
                    del obj['__class__']
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
