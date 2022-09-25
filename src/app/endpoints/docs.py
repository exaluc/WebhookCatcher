# -*- coding: utf-8 -*-
# Lucian BLETAN

from fastapi import APIRouter
from fastapi.openapi.docs import get_swagger_ui_html
from config import settings

router = APIRouter()

@router.get("/", include_in_schema=False)
def overridden_swagger():
	return get_swagger_ui_html(
     openapi_url="/openapi.json", 
     title=f"{settings.title} - Swagger UI",
     swagger_favicon_url=""
     )