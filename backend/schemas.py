from pydantic import BaseModel


class EmployeeCreate(BaseModel):

    employee_name: str

    department: str

    salary: float

    email: str


class EmployeeResponse(EmployeeCreate):

    id: int

    class Config:

        from_attributes = True