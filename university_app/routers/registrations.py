from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal

router = APIRouter(prefix="/registrations", tags=["Registrations"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Registration)
def create_registration(reg: schemas.RegistrationCreate, db: Session = Depends(get_db)):
    new_reg = models.Registration(**reg.dict())
    db.add(new_reg)
    db.commit()
    db.refresh(new_reg)
    return new_reg


@router.get("/", response_model=list[schemas.Registration])
def get_regs(db: Session = Depends(get_db)):
    return db.query(models.Registration).all()
