from sqlalchemy.orm import Session
from fastapi import HTTPException
from services.warehouse import models, schemas

# ============================================================
#                      ITEMS
# ============================================================

def get_item(db: Session, name: str):
    item = db.query(models.Item).filter(models.Item.name == name).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


def get_items(db: Session):
    return db.query(models.Item).all()


def create_item(db: Session, item: schemas.ItemCreate):

    category = db.query(models.Category).filter(models.Category.name == item.category_name).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    section = db.query(models.Section).filter(models.Section.code == item.section_code).first()
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")

    new_item = models.Item(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def update_item(db: Session, name: str, item_update: schemas.ItemUpdate):
    item = db.query(models.Item).filter(models.Item.name == name).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if item_update.category_name is not None:
        category = db.query(models.Category).filter(models.Category.name == item_update.category_name).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

    if item_update.section_code is not None:
        section = db.query(models.Section).filter(models.Section.code == item_update.section_code).first()
        if not section:
            raise HTTPException(status_code=404, detail="Section not found")

    update_data = item_update.dict(exclude_unset=True)

    for field, value in update_data.items():
        setattr(item, field, value)

    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, name: str):
    item = db.query(models.Item).filter(models.Item.name == name).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"detail": "Item deleted successfully"}


# ============================================================
#                 CATEGORIES
# ============================================================

def get_categories(db: Session):
    return db.query(models.Category).all()


def create_category(db: Session, category: schemas.CategoryCreate):
    new_category = models.Category(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


# ============================================================
#                   SECTIONS
# ============================================================

def get_sections(db: Session):
    return db.query(models.Section).all()


def create_section(db: Session, section: schemas.SectionCreate):
    new_section = models.Section(**section.dict())
    db.add(new_section)
    db.commit()
    db.refresh(new_section)
    return new_section