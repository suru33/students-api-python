from datetime import datetime
from uuid import uuid4

from sqlalchemy.orm import Session

from app.models import Branch
from app.schemas import BranchRequest


def create_branch(db: Session, request: BranchRequest):
    branch = Branch(
        id=uuid4(),
        short_name=request.short_name,
        name=request.name,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(branch)
    db.commit()
    db.refresh(branch)
    return branch


def get_branch_by_id(db: Session, branch_id: str):
    return db.query(Branch).filter(Branch.id == branch_id).first()


def get_all_branches(db: Session):
    return db.query(Branch).all()
