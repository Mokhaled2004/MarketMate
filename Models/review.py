#!/usr/bin/python3
"""Defines the Review class."""

from MarketMate.Models.base_model import BaseModel

class Review(BaseModel):
    
    """Represents a review """
    
    prdocut_id = ""
    user_id = ""
    rating = 0
    text = ""
    
 
