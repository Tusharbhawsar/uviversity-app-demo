from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal

router = APIRouter(prefix="/students", tags=["Students"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Student)
def create_student(stu: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_stu = models.Student(**stu.dict())
    db.add(new_stu)
    db.commit()
    db.refresh(new_stu)
    return new_stu


@router.get("/", response_model=list[schemas.Student])
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()
