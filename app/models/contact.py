"""
Contact model for storing contact form submissions
"""
from sqlalchemy import Column, String, Text, Boolean
from app.core.database import Base
from app.models.base import BaseModel


class Contact(Base, BaseModel):
    """
    Contact form submission model
    """
    __tablename__ = "contacts"

    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, index=True)
    subject = Column(String(500), nullable=True)
    message = Column(Text, nullable=False)
    phone = Column(String(50), nullable=True)
    is_read = Column(Boolean, default=False, nullable=False)
    is_replied = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<Contact(id={self.id}, name={self.name}, email={self.email})>"

