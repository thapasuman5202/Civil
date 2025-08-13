from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from ..db.base import Base


class SiteTwin(Base):
    __tablename__ = "site_twins"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    region_code = Column(String, nullable=True)
    lat = Column(Float, nullable=True)
    lon = Column(Float, nullable=True)
    meta = Column(JSON, nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
