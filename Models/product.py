#!/usr/bin/python3
"""Defines the Product  class."""

from Models.base_model import BaseModel

class Product(BaseModel):
    
    """Represents a product """
    
    name = ""
    description = ""
    price = 0
    stock = 0
    category = ""
    image = ""