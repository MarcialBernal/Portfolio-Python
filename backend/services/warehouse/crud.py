from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas


def get_item(db:Session, item_id:int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db:Session):
    return db.query(models.Item).all()

def create_item():
    pass

def update_item():
    pass

def delete_item():
    pass