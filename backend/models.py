from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import TIMESTAMP
from sqlalchemy.sql import func

from backend.database import Base


class Employee(Base):

    __tablename__ = "employees"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_name = Column(String)

    department = Column(String)

    salary = Column(Float)

    email = Column(
        String,
        unique=True
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True
    )

    password = Column(String)