#!/usr/bin/python3
"""Defines the Review class."""
from sqlalchemy.ext.declarative import declarative_base
from Models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Review(BaseModel):
    
    """Represents a review """
    
    
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    market_id = Column(String(60), ForeignKey("market.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("user.id"), nullable=False)
    rating = Column(Float, nullable=False)
    text = Column(String(1024), nullable=False)
    
 
