from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....core.deps import get_db
from ....models import Variant as VariantModel
from ....schemas import Variant as VariantSchema, VariantCreate

router = APIRouter(prefix="/variants", tags=["variants"])


@router.post("/", response_model=VariantSchema)
def create_variant(data: VariantCreate, db: Session = Depends(get_db)):
    variant = VariantModel(**data.model_dump())
    db.add(variant)
    db.commit()
    db.refresh(variant)
    return variant


@router.post("/{variant_id}/score", response_model=VariantSchema)
def score_variant(variant_id: int, db: Session = Depends(get_db)):
    variant = db.get(VariantModel, variant_id)
    if not variant:
        raise HTTPException(status_code=404, detail="Not found")
    variant.score_primary = float(len(variant.name))
    variant.scores_json = {"length": variant.score_primary}
    db.commit()
    db.refresh(variant)
    return variant


@router.get("/", response_model=list[VariantSchema])
def list_variants(db: Session = Depends(get_db)):
    return db.query(VariantModel).all()
