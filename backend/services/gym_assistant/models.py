from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, text


# ============================================================
#                      USERS (GYM ASSISTANT)
# ============================================================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    age = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    training_days = Column(Integer, nullable=False)
    training_hours = Column(Float, nullable=False)
    goal = Column(String(100), nullable=False)
    experience = Column(String(50))

    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

