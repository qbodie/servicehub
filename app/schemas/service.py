from pydantic import BaseModel

class ServiceCreate(BaseModel):
    title: str
    description: str | None = None
    price: float
    is_active: bool = True

    class Config:
        orm_mode = True


class ServiceUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    price: float | None = None
    is_active: bool | None = None

    class Config:
        orm_mode = True


class ServiceOut(BaseModel):
    id: int
    title: str
    description: str | None
    price: float
    is_active: bool
    owner_id: int

    class Config:
        orm_mode = True