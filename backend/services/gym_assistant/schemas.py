from datetime import datetime
from pydantic import BaseModel
from typing import Optional

# ============================================================
#                      USERS (GYM ASSISTANT)
# ============================================================
class UserBase(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    training_days: int       
    training_hours: float    
    goal: str                
    experience: Optional[str] = None 

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    training_days: Optional[int] = None
    training_hours: Optional[float] = None
    goal: Optional[str] = None
    experience: Optional[str] = None

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True