"""
Base models and mixins
"""
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func


class TimestampMixin:
    """
    Mixin to add timestamp fields to models
    """
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class BaseModel(TimestampMixin):
    """
    Base model with common fields
    """
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

