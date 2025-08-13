from pydantic import BaseModel


class ConstraintBase(BaseModel):
    site_twin_id: int
    kind: str
    value: str


class ConstraintCreate(ConstraintBase):
    pass


class Constraint(ConstraintBase):
    id: int

    class Config:
        from_attributes = True
