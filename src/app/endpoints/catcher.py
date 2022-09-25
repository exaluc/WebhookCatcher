# -*- coding: utf-8 -*-
# Lucian BLETAN

import uuid
from fastapi import APIRouter, Request
from utils.dates import getDtNow
from loguru import logger
from fastapi.responses import JSONResponse
import json
from utils.database import DbConnector

router = APIRouter()

db = DbConnector()

def dbInsertModel(h, d):
    r = dict()
    r['uuid'] = str(uuid.uuid4())
    r['date_received'] = getDtNow()
    r['headers'] = h
    r['request'] = d
    return r

@router.post("/")
async def post_webhook(request: Request):
    try:
        h = dict(request.headers)
        logger.debug(json.dumps(h))
        d = await request.json()
        logger.debug(json.dumps(d))
        r = dbInsertModel(h, d)
        db.insert(r)
        return JSONResponse(r)
    except Exception as res:    
        return res

@router.get("/")
async def get_webhooks(request: Request):
    try:
        return JSONResponse(db.getAll())
    except Exception as res:    
        return res

@router.put("/")
async def put_webhook(request: Request):
    try:
        h = dict(request.headers)
        logger.debug(json.dumps(h))
        d = await request.json()
        logger.debug(json.dumps(d))
        r = dbInsertModel(h, d)
        db.insert(r)
        return JSONResponse(r)
    except Exception as res:    
        return res