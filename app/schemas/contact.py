"""
Contact schemas for request/response validation
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class ContactBase(BaseModel):
    """
    Base schema for contact
    """
    name: str = Field(..., min_length=1, max_length=255, description="Contact name")
    email: EmailStr = Field(..., description="Contact email address")
    subject: Optional[str] = Field(None, max_length=500, description="Message subject")
    message: str = Field(..., min_length=1, description="Contact message")
    phone: Optional[str] = Field(None, max_length=50, description="Contact phone number")


class ContactCreate(ContactBase):
    """
    Schema for creating a contact
    """
    pass


class ContactUpdate(BaseModel):
    """
    Schema for updating contact status
    """
    is_read: Optional[bool] = None
    is_replied: Optional[bool] = None


class ContactResponse(ContactBase):
    """
    Schema for contact response
    """
    id: int
    is_read: bool
    is_replied: bool
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class ContactList(BaseModel):
    """
    Schema for paginated contact list
    """
    total: int
    page: int
    page_size: int
    contacts: list[ContactResponse]

