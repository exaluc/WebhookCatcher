# -*- coding: utf-8 -*-
# Lucian BLETAN

from fastapi import APIRouter
from fastapi.openapi.docs import get_redoc_html
from config import settings

router = APIRouter()

@router.get("/", include_in_schema=False)
def overridden_redoc():
	return get_redoc_html(
     openapi_url="/openapi.json", 
     title=f"{settings.title} - ReDoc",
     redoc_favicon_url=""
     )