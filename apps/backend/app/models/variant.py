from sqlalchemy import Column, Integer, String, ForeignKey, Float, JSON
from ..db.base import Base


class Variant(Base):
    __tablename__ = "variants"

    id = Column(Integer, primary_key=True)
    site_twin_id = Column(Integer, ForeignKey("site_twins.id"))
    name = Column(String, nullable=False)
    summary = Column(String, nullable=True)
    score_primary = Column(Float, default=0.0)
    scores_json = Column(JSON, default={})
    status = Column(String, default="draft")
