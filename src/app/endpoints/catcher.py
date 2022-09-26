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

@router.post("/{item_dataset}")
async def post_webhook(request: Request, item_dataset: str):
    try:
        h = dict(request.headers)
        logger.debug(json.dumps(h))
        d = await request.json()
        logger.debug(json.dumps(d))
        r = dbInsertModel(h, d)
        db.insert(r, item_dataset)
        return JSONResponse(r)
    except Exception as res:    
        return res

@router.get("/{item_dataset}")
async def get_webhooks(item_dataset: str, limit: int):
    try:
        return JSONResponse(db.getAll(item_dataset, limit))
    except Exception as res:    
        return res

@router.put("/{item_dataset}")
async def put_webhook(request: Request, item_dataset: str):
    try:
        h = dict(request.headers)
        logger.debug(json.dumps(h))
        d = await request.json()
        logger.debug(json.dumps(d))
        r = dbInsertModel(h, d)
        db.insert(r, item_dataset)
        return JSONResponse(r)
    except Exception as res:    
        return res