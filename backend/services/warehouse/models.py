from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, text
from sqlalchemy.orm import relationship


###
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    items = relationship("Item", back_populates="category")


###
class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True)
    code = Column(String(2), nullable=False, unique=True) 

    items = relationship("Item", back_populates="section")


###
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    quantity = Column(Integer, default=0)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))
    location_id = Column(Integer, ForeignKey("sections.id"))
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    

    category = relationship("Category", back_populates="items")
    location = relationship("Section", back_populates="items")