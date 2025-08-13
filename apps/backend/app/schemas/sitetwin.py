from pydantic import BaseModel
from typing import Optional

class SiteTwinBase(BaseModel):
    name: str
    region_code: Optional[str] = None
    meta: Optional[dict] = None

class SiteTwinCreate(SiteTwinBase):
    pass

class SiteTwin(SiteTwinBase):
    id: int

    class Config:
        from_attributes = True
