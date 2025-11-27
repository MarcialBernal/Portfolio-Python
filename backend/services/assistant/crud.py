from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

# ============================================================
#                      USERS (GYM ASSISTANT)
# ============================================================

def get_user(db: Session, user_name: str):
    user = db.query(models.User).filter(models.User.name == user_name).all()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_user_by_name_and_age(db: Session, name: str, age: int):
    return (db.query(models.User).filter(models.User.name == name, models.User.age == age).all())


def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for field, value in user_update.dict(exclude_unset=True).items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}