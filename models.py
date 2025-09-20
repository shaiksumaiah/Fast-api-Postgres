# models.py
from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from database import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False, default=0.0)
    is_offer = Column(Boolean, default=False)
