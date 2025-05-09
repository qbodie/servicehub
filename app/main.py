from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import auth, user, service

app = FastAPI()
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(auth.router, prefix="/users", tags=["users"])
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(service.router, prefix="/services", tags=["services"])

@app.get("/ping")
async def ping():
    return {"status": "ok"}

