#!/usr/bin/python3
"""Amenity model for DBStorage Many-to-Many with Place"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship(
            'Place', secondary='place_amenity', viewonly=False,
            back_populates='amenities')
