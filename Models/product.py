#!/usr/bin/python3
"""Defines the Product  class."""

from Models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Product(BaseModel):
    
    """Represents a product """
    __tablename__ = "products"
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category = Column(String(128), nullable=False)
    