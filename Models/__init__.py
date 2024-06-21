#!/usr/bin/python3

from Models.engine.file_storage import FileStorage
from Models.engine.db_storage import DBStorage
from Models.base_model import BaseModel
from Models.user import User
from Models.product import Product
from Models.order import Order
from Models.review import Review
from os import getenv


if getenv("MarketMate_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
