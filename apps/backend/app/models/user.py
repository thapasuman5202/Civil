from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="engineer")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
