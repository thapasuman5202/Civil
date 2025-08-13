from pydantic import BaseModel
from typing import Dict, Optional


class VariantBase(BaseModel):
    site_twin_id: int
    name: str
    summary: Optional[str] = None


class VariantCreate(VariantBase):
    pass


class Variant(VariantBase):
    id: int
    score_primary: float
    scores_json: Optional[Dict[str, float]] = None
    status: str

    class Config:
        from_attributes = True
