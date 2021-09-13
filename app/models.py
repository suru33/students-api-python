from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import DATE, TIMESTAMP, UUID

from app.database import Base


class Branch(Base):
    __tablename__ = 'branch'

    id = Column(name='b_id', type_=UUID(as_uuid=True), primary_key=True, index=True)
    short_name = Column(name='b_short_name', type_=String, nullable=False)
    name = Column(name='b_name', type_=String, nullable=False)
    created_at = Column(name='b_created_at', type_=TIMESTAMP, nullable=False)
    updated_at = Column(name='b_updated_at', type_=TIMESTAMP)


class Student(Base):
    __tablename__ = 'student'

    id = Column(name='s_id', type_=UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(name='s_name', type_=String, nullable=False)
    branch = Column(name='s_branch', type_=UUID, nullable=False)
    year = Column(name='s_year', type_=Integer, nullable=False)
    dob = Column(name='s_dob', type_=DATE, nullable=False)
    email = Column(name='s_email', type_=String, nullable=False)
    phone = Column(name='s_phone', type_=String, nullable=False)
    created_at = Column(name='s_created_at', type_=TIMESTAMP, nullable=False)
    updated_at = Column(name='s_updated_at', type_=TIMESTAMP)
