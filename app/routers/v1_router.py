from fastapi import APIRouter
from app.routers.v1 import ai,claims,patients
 
v1_router=APIRouter(prefix="/v1")
v1_router.include_router(ai.router)
v1_router.include_router(claims.router)
v1_router.include_router(patients.router)
