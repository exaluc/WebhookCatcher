# -*- coding: utf-8 -*-
# Lucian BLETAN

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def index():
    return {"webhook": "catcher"}