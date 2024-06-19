#!/usr/bin/python3
"""Defines the User class."""

from Models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Models.review import Review


class User(BaseModel, Base):
    
    """Represents a user for the application."""
    
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    address = Column(String(128),nullable=False)
    phone = Column(String(20), nullable=False)
    orders = relationship("order", backref="user")
        reviews = relationship("review", backref="user")
    
    
    
