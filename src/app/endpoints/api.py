# -*- coding: utf-8 -*-
# Lucian BLETAN

from fastapi import APIRouter

from endpoints import index, healthcheck, docs, redoc, catcher

theRouter = APIRouter()

theRouter.include_router(index.router)
theRouter.include_router(healthcheck.router, prefix="/healthcheck", tags=["health check"])
theRouter.include_router(docs.router, prefix="/docs", tags=["swagger doc"])
theRouter.include_router(redoc.router, prefix="/redoc", tags=["redoc doc"])
theRouter.include_router(catcher.router, prefix="/catcher", tags=["catcher"])