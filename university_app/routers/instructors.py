from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal

router = APIRouter(prefix="/instructors", tags=["Instructors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Instructor)
def create_instructor(ins: schemas.InstructorCreate, db: Session = Depends(get_db)):
    new_ins = models.Instructor(**ins.dict())
    db.add(new_ins)
    db.commit()
    db.refresh(new_ins)
    return new_ins


@router.get("/", response_model=list[schemas.Instructor])
def get_instructors(db: Session = Depends(get_db)):
    return db.query(models.Instructor).all()
