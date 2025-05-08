from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud import service as crud_service
from app.schemas.service import ServiceCreate, ServiceUpdate, ServiceOut
from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=ServiceOut)
def create_service_route(
    service_in: ServiceCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    service = crud_service.create_service(db, service_in, current_user.id)
    return service


@router.get("/me", response_model=list[ServiceOut])
def get_my_services(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_service.get_user_services(db, current_user.id)


@router.get("/{service_id}", response_model=ServiceOut)
def get_service_route(service_id: int, db: Session = Depends(get_db)):
    service = crud_service.get_service(db, service_id)
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

@router.get("/", response_model=list[ServiceOut])
def get_services_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    services = crud_service.get_services(db, skip=skip, limit=limit)
    return services

@router.put("/{service_id}", response_model=ServiceOut)
def update_service_route(
    service_id: int, service_in: ServiceUpdate, db: Session = Depends(get_db)
):
    service = crud_service.update_service(db, service_id, service_in)
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

@router.delete("/{service_id}", response_model=dict)
def delete_service_route(service_id: int, db: Session = Depends(get_db)):
    success = crud_service.delete_service(db, service_id)
    if not success:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"detail": "Service deleted"}


