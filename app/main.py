from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import auth

app = FastAPI()
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/ping")
async def ping():
    return {"status": "ok"}

