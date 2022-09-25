# -*- coding: utf-8 -*-
# Lucian BLETAN

from datetime import datetime

def getDtNow():
    now = datetime.now()
    dtString = now.isoformat()
    return dtString

def getDtNowStrftime():
    now = datetime.now()
    dtString = now.strftime("%d/%m/%Y %H:%M:%S")
    return dtString