#!/usr/bin/python3
"""Defines the Order class."""

from sqlalchemy.ext.declarative import declarative_base
from Models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from Models.user import User

class Order(BaseModel, Base):
    
    __tablename__ = "orders"
    price = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    market_name = Column(String(128), nullable=False)
    user = relationship("user", back_populates="orders")
    
    

        
