from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db

router = APIRouter()

@router.get("/items", response_model=list[schemas.Item])
def get_items(db: Session = Depends(get_db)):
    return crud.get_items(db)