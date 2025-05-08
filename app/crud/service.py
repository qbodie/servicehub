from sqlalchemy.orm import Session
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceUpdate


def create_service(db: Session, service_in: ServiceCreate, owner_id: int) -> Service:
    service = Service(
        title=service_in.title,
        description=service_in.description,
        price=service_in.price,
        is_active=service_in.is_active,
        owner_id=owner_id,
    )
    db.add(service)
    db.commit()
    db.refresh(service)
    return service


def get_service(db: Session, service_id: int) -> Service | None:
    return db.query(Service).filter(Service.id == service_id).first()


def get_services(db: Session, skip: int = 0, limit: int = 100) -> list[Service]:
    return db.query(Service).offset(skip).limit(limit).all()


def update_service(db: Session, service_id: int, service_in: ServiceUpdate) -> Service | None:
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        return None

    if service_in.title is not None:
        service.title = service_in.title
    if service_in.description is not None:
        service.description = service_in.description
    if service_in.price is not None:
        service.price = service_in.price
    if service_in.is_active is not None:
        service.is_active = service_in.is_active

    db.commit()
    db.refresh(service)
    return service


def delete_service(db: Session, service_id: int) -> bool:
    service = db.query(Service).filter(Service.id == service_id).first()
    if service:
        db.delete(service)
        db.commit()
        return True
    return False


def get_all_services(db: Session) -> list[Service]:
    return db.query(Service).all()


def get_service_by_id(db: Session, service_id: int) -> Service | None:
    return db.query(Service).filter(Service.id == service_id).first()


def get_user_services(db: Session, user_id: int) -> list[Service]:
    return db.query(Service).filter(Service.owner_id == user_id).all()

