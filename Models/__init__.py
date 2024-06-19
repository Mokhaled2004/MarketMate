#!/usr/bin/python3

from Models.engine.file_storage import FileStorage
from Models.engine.db_storage import DBStorage
import Models.base_model
import Models.user
import Models.order
import Models.review
import Models.product
from os import getenv


if getenv("MarketMate_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
