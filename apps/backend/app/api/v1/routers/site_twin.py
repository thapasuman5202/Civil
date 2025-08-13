from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....core.deps import get_db
from ....models import SiteTwin as SiteTwinModel
from ....schemas import SiteTwin, SiteTwinCreate
from .auth import get_current_user

router = APIRouter(prefix="/sitetwins", tags=["sitetwins"])


@router.post("/", response_model=SiteTwin)
def create_site_twin(data: SiteTwinCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    obj = SiteTwinModel(**data.model_dump(), created_by=user.id)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.get("/", response_model=list[SiteTwin])
def list_site_twins(db: Session = Depends(get_db)):
    return db.query(SiteTwinModel).all()


@router.get("/{st_id}", response_model=SiteTwin)
def get_site_twin(st_id: int, db: Session = Depends(get_db)):
    obj = db.get(SiteTwinModel, st_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj
