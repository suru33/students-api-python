from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.repositories import branch_repository as repository, student_repository
from app.schemas import BranchRequest, BranchResponse, StudentRequest, StudentResponse

router = APIRouter(prefix="/branch", tags=["branch"])


@router.get("/all", response_model=List[BranchResponse])
async def get_all_branches(db: Session = Depends(get_db)):
    return repository.get_all_branches(db)


@router.get("/{branch_id}", response_model=BranchResponse)
async def get_branch_by_id(branch_id: UUID, db: Session = Depends(get_db)):
    return repository.get_branch_by_id(db, branch_id)


@router.post("/", response_model=BranchResponse, status_code=status.HTTP_201_CREATED)
async def create_branch(request: BranchRequest, db: Session = Depends(get_db)):
    return repository.create_branch(db, request)


@router.post("/{branch_id}/student", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
async def create_student(request: StudentRequest, branch_id: UUID, db: Session = Depends(get_db)):
    return student_repository.create_student(db, branch_id, request)
