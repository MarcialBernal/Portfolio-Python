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

class Item(ItemBase):
    id: int
    created_at: str
    class Config:
        orm_mode = True