from sqlalchemy import Column, Integer, String, ForeignKey
from ..db.base import Base


class Constraint(Base):
    __tablename__ = "constraints"

    id = Column(Integer, primary_key=True)
    site_twin_id = Column(Integer, ForeignKey("site_twins.id"))
    kind = Column(String)
    value = Column(String)
    units = Column(String, nullable=True)
    source = Column(String, nullable=True)
    note = Column(String, nullable=True)
