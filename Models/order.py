#!/usr/bin/python3
"""Defines the Order class."""

from MarketMate.Models.base_model import BaseModel

class Order(BaseModel):
    
    name = ""
    price = 0.0
    quantity = 0
    user_id = ""
    product_id = ""
    status = "pending"
    payment_id = ""
    shipping_id = ""
    tracking_id = ""
    tracking_url = ""
    tracking_status = ""
    tracking_location = ""
    tracking_date = ""
    tracking_notes = ""
    tracking_delivered = False
    tracking_delivered_date = ""
    tracking_delivered_location = ""
    tracking_delivered_notes = ""
    tracking_delivered_signature = ""
    tracking_delivered_signature_url = ""
    tracking_delivered_signature_date = ""
    tracking_delivered_signature_location = ""
    tracking_delivered_signature_notes = ""

        
