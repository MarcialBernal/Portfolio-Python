from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.warehouse import crud, schemas
from services.warehouse.database import get_db

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


@router.put("/items/{name}", response_model=schemas.Item)
def update_item(name: str, item_update: schemas.ItemUpdate, db: Session = Depends(get_db)):
    return crud.update_item(db, name, item_update)


@router.delete("/items/{name}")
def delete_item(name: str, db: Session = Depends(get_db)):
    return crud.delete_item(db, name)



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