# -*- coding: utf-8 -*-
# Lucian BLETAN

from fastapi import APIRouter
from utils.dates import getDtNow
import uuid

router = APIRouter()

@router.get("/")
def health_check():
    return {"date": str(getDtNow()),
            "id": uuid.uuid4()}