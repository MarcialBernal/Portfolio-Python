from datetime import datetime
from pydantic import BaseModel
from typing import Optional

# ---- Category ----
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    class Config:
        orm_mode = True


# ---- Section ----
class SectionBase(BaseModel):
    code: str

class SectionCreate(SectionBase):
    pass

class Section(SectionBase):
    id: int
    class Config:
        orm_mode = True


# ---- Item ----
class ItemBase(BaseModel):
    name: str
    quantity: Optional[int] = 0
    price: Optional[float] = None
    category_name: str
    section_code: str

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    category_name: Optional[str] = None
    section_code: Optional[str] = None

    class Config:
        orm_mode = True

class Item(ItemBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True