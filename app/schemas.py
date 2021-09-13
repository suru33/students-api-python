from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel


class BranchRequest(BaseModel):
    short_name: str
    name: str


class BranchResponse(BaseModel):
    id: UUID
    short_name: str
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class StudentRequest(BaseModel):
    name: str
    branch: str
    year: int
    dob: str
    email: str
    phone: str


class StudentResponse(BaseModel):
    id: UUID
    name: str
    branch: str
    year: int
    dob: date
    email: str
    phone: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
