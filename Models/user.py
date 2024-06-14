#!/usr/bin/python3
"""Defines the User class."""

from MarketMate.Models.base_model import BaseModel

class User(BaseModel):
    
    """Represents a user for the application."""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    
