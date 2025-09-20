# schemas.py
from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    is_offer: Optional[bool] = False

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_offer: Optional[bool] = None

class ItemInDBBase(ItemBase):
    id: int

    class Config:
        orm_mode = True

class Item(ItemInDBBase):
    pass
