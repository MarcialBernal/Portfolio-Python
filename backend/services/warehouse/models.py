from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, text
from sqlalchemy.orm import relationship


# ============================================================
#                 CATEGORIES
# ============================================================
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    items = relationship("Item", back_populates="category")


# ============================================================
#                   SECTIONS
# ============================================================
class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True)
    code = Column(String(2), nullable=False, unique=True) 

    items = relationship("Item", back_populates="section")


# ============================================================
#                      ITEMS
# ============================================================
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    quantity = Column(Integer, default=0)
    price = Column(Float)
    category_name = Column(String, ForeignKey("categories.name"))
    section_code = Column(String, ForeignKey("sections.code"))
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    

    category = relationship("Category", back_populates="items")
    section = relationship("Section", back_populates="items")