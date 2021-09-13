from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, conint, constr


class BranchRequest(BaseModel):
    short_name: constr(strict=True, min_length=3, max_length=10)
    name: constr(strict=True, min_length=3, max_length=100)


class BranchResponse(BaseModel):
    id: UUID
    short_name: str
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class StudentRequest(BaseModel):
    name: constr(strict=True, min_length=3, max_length=100)
    year: conint(strict=True, ge=1, le=4)
    dob: date
    email: EmailStr
    phone: constr(strict=True, min_length=5, max_length=20)


class StudentResponse(BaseModel):
    id: UUID
    name: str
    branch: UUID
    year: conint(strict=True, ge=1, le=4)
    dob: date
    email: EmailStr
    phone: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
