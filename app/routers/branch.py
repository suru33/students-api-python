from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.repositories import branch_repository as repository
from app.schemas import BranchRequest, BranchResponse

router = APIRouter(prefix="/branch", tags=["branch"])


@router.get("/all", response_model=List[BranchResponse])
async def get_all_branches(db: Session = Depends(get_db)):
    return repository.get_all_branches(db)


@router.get("/{branch_id}", response_model=BranchResponse)
async def get_branch_by_id(branch_id, db: Session = Depends(get_db)):
    branch = repository.get_branch_by_id(db, branch_id)
    if branch is None:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch


@router.post("/", response_model=BranchResponse)
async def create_branch(request: BranchRequest, db: Session = Depends(get_db)):
    return repository.create_branch(db, request)
