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

    def insert(self, data, table):
        try:
            d = self.dbClient.table(table)
            return d.insert(data)
        except Exception as e:
            logger.warning(e)

    def getAll(self, table, limit):
        try:
            d = self.dbClient.table(table)
            return d.all()[-limit:]
        except Exception as e:
            logger.warning(e)
