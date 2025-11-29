from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, schemas
from database import get_db

router = APIRouter()

# ============================================================
#                        USERS (GYM ASSISTANT)
# ============================================================

@router.get("/users/{user_name}", response_model=list[schemas.User])
def get_user(user_name: str, db: Session = Depends(get_db)):
    return crud.get_user(db, user_name)


@router.get("/users/{user_name}/{age}", response_model=list[schemas.User])
def get_user_by_name_and_age(user_name: str, age: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_name_and_age(db, user_name, age)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users", response_model=list[schemas.User])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@router.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user_update)


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)