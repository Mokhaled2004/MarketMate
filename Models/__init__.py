#!/usr/bin/python3

from engine.file_storage import FileStorage
from engine.db_storage import DBStorage
from Models.base_model import BaseModel
from Models.user import User
from Models.review import Review
from os import getenv


if getenv("MarketMate_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
