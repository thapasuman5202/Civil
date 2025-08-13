from fastapi import APIRouter
from .routers import auth, site_twin, variant, constraints, health

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(auth.router)
api_router.include_router(site_twin.router)
api_router.include_router(variant.router)
api_router.include_router(constraints.router)
api_router.include_router(health.router)
