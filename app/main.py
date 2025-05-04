from fastapi import FastAPI
from app.core.config import settings

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"status": "ok"}

