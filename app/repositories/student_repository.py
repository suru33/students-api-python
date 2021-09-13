from datetime import datetime
from uuid import uuid4

from sqlalchemy.orm import Session

from app.models import Student
from app.schemas import StudentRequest


def create_student(db: Session, request: StudentRequest):
    student = Student(
        id=uuid4(),
        name=request.name,
        branch=request.branch,
        year=request.year,
        dob=request.dob,
        email=request.email,
        phone=request.phone,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def get_student_by_id(db: Session, student_id: str):
    return db.query(Student).filter(Student.id == student_id).first()


def get_all_students(db: Session):
    return db.query(Student).all()
