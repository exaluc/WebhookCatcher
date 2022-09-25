# -*- coding: utf-8 -*-
# Lucian BLETAN

from tinydb import TinyDB
from config import settings
from loguru import logger

class DbConnector:
    def __init__(self) -> None:
        self.dbClient = None
        self.connect()

    def connect(self):
        db = TinyDB(settings.dataPath)
        self.dbClient = db

    def insert(self, data):
        try:
            return self.dbClient.insert(data)
        except Exception as e:
            logger.warning(e)

    def getAll(self):
        try:
            return self.dbClient.all()
        except Exception as e:
            logger.warning(e)
