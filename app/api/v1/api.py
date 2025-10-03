"""
Main API router
"""
from fastapi import APIRouter
from app.api.v1.endpoints import contacts

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(
    contacts.router,
    prefix="/contacts",
    tags=["contacts"]
)

