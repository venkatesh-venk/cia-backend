"""
Database models
"""
from app.core.database import Base
from app.models import base

# Import all models here to make them available for Alembic
__all__ = ["Base", "base"]

