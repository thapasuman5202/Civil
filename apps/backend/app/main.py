from fastapi import FastAPI
from .api.v1 import api_router

app = FastAPI(title="Civil Stage Zero")
app.include_router(api_router)


@app.get("/")
def read_root() -> dict:
    return {"message": "ok"}
