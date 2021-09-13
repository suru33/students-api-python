from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.repositories import student_repository as repository
from app.schemas import StudentResponse

router = APIRouter(prefix="/student", tags=["student"])


@router.get("/all", response_model=List[StudentResponse])
async def get_all_students(db: Session = Depends(get_db)):
    return repository.get_all_students(db)


@router.get("/{student_id}", response_model=StudentResponse)
async def get_student_by_id(student_id: UUID, db: Session = Depends(get_db)):
    student = repository.get_student_by_id(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student



