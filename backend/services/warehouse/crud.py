from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

#---------
def get_item(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

#---------
def get_items(db:Session):
    return db.query(models.Item).all()

#---------
def create_item(db: Session, item: schemas.ItemCreate):

    category = db.query(models.Category).filter(models.Category.id == item.category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    section = db.query(models.Section).filter(models.Section.id == item.location_id).first()
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")

    new_item = models.Item(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

#---------
def update_item(db: Session, item_id: int, item_update: schemas.ItemUpdate):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if item_update.category_id is not None:
        category = db.query(models.Category).filter(models.Category.id == item_update.category_id).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

    if item_update.location_id is not None:
        section = db.query(models.Section).filter(models.Section.id == item_update.location_id).first()
        if not section:
            raise HTTPException(status_code=404, detail="Section not found")

    update_data = item_update.dict(exclude_unset=True)

    for field, value in update_data.items():
        setattr(item, field, value)

    db.commit()
    db.refresh(item)

    return item

#----------
def delete_item(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    
    return {"detail": "Item deleted successfully"}