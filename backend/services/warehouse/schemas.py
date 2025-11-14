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
    category_id: int
    location_id: int

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    category_id: Optional[int] = None
    location_id: Optional[int] = None

    class Config:
        orm_mode = True

class Item(ItemBase):
    id: int
    created_at: str
    class Config:
        orm_mode = True