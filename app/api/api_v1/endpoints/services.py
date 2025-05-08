from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import service as crud_service

from app.api.routes.service import router
from app.db.session import get_db
from app.schemas.service import ServiceOut


@router.get("/", response_model=list[ServiceOut])
def get_services(db: Session = Depends(get_db)):
    return crud_service.get_all_services(db)


@router.get("/{service_id}", response_model=ServiceOut)
def get_service(service_id: int, db: Session = Depends(get_db)):
    service = crud_service.get_service_by_id(db, service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

