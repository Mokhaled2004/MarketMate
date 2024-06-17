#!/usr/bin/python3
"""Module base_model

This Module contains a definition for BaseModel Class
"""
import uuid
from datetime import datetime

class BaseModel:
    
    """BaseModel Class"""
    
    def __init__(self, *args, **kwargs):
        
        """BaseModel Constructor"""
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if kwargs is not None and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
                    
        else:
            from Models import storage
            storage.new(self)   
            
    def __str__(self):
        """String Representation of BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        
    def save(self):
        """Save Method"""
        self.updated_at = datetime.now()
        from Models import storage
        storage.save()
            
    def to_dict(self):
        """to_dict Method"""
        rdict = self.__dict__.copy()
        rdict['__class__'] = self.__class__.__name__
        rdict['created_at'] = self.created_at.isoformat()
        rdict['updated_at'] = self.updated_at.isoformat()
        return rdict
