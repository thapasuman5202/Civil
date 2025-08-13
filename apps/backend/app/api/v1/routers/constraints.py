from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ....core.deps import get_db
from ....models import Constraint
from ....schemas import Constraint, ConstraintCreate

router = APIRouter(prefix="/constraints", tags=["constraints"])


@router.post("/", response_model=Constraint)
def create_constraint(data: ConstraintCreate, db: Session = Depends(get_db)):
    obj = Constraint(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.get("/", response_model=list[Constraint])
def list_constraints(db: Session = Depends(get_db)):
    return db.query(Constraint).all()
