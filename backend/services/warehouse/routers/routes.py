from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, schemas
from database import get_db

router = APIRouter()

# ============================================================
#                        ITEMS
# ============================================================

@router.get("/items", response_model=list[schemas.Item])
def get_items(db: Session = Depends(get_db)):
    return crud.get_items(db)


@router.get("/items/{name}", response_model=schemas.Item)
def get_item(name: str, db: Session = Depends(get_db)):
    return crud.get_item(db, name)


@router.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)


@router.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item_update: schemas.ItemUpdate, db: Session = Depends(get_db)):
    return crud.update_item(db, item_id, item_update)


@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crud.delete_item(db, item_id)



# ============================================================
#                     CATEGORIES
# ============================================================

@router.get("/categories", response_model=list[schemas.Category])
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.post("/categories", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)



# ============================================================
#                     SECTIONS
# ============================================================

@router.get("/sections", response_model=list[schemas.Section])
def get_sections(db: Session = Depends(get_db)):
    return crud.get_sections(db)


@router.post("/sections", response_model=schemas.Section)
def create_section(section: schemas.SectionCreate, db: Session = Depends(get_db)):
    return crud.create_section(db, section)