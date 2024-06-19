#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import Models
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from Models.base_model import Base,BaseModel
from Models.user import User
from Models.order import Order
from Models.review import Review
from Models.product import Product

classes = {"Order": Order, "Product": Product,
           "User": User, "Review": Review}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None
    

def __init__(self):
        """Instantiate a DBStorage object"""
        MarketMate_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        MarketMate_PWD = getenv('HBNB_MYSQL_PWD')
        MarketMate_HOST = getenv('HBNB_MYSQL_HOST')
        MarketMate_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        MarketMate_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format( MarketMate_MYSQL_USER,
                                            MarketMate_MYSQL_PWD,
                                            MarketMate_MYSQL_HOST,
                                            MarketMate_MYSQL_DB))
        
        if MarketMate_ENV == "test":
            Base.metadata.drop_all(self.__engine)
            
def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)
    
    
def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)
        
def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

def delete(self, obj=None):
    """delete from the current database session obj if not None"""
    if obj is not None:
        self.__session.delete(obj)  
        
def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
        
        
def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
        
def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None
    
def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(Models.storage.all(clas).values())
        else:
            count = len(Models.storage.all(cls).values())

        return count
             
        