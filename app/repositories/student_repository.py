from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy.orm import Session

from app.exceptions import EntityNotFoundException
from app.models import Student
from app.repositories import branch_repository
from app.schemas import StudentRequest


def create_student(db: Session, branch_id: UUID, request: StudentRequest):
    branch = branch_repository.get_branch_by_id(db, branch_id)

    student = Student(
        id=uuid4(),
        name=request.name,
        branch=branch.id,
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


def get_student_by_id(db: Session, student_id: UUID):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        return student

    raise EntityNotFoundException('student', student_id)


def get_all_students(db: Session):
    return db.query(Student).all()
