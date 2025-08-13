from fastapi import APIRouter

router = APIRouter(tags=["admin"])


@router.get("/health")
def health() -> dict:
    return {"status": "ok"}
