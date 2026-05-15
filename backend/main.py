from fastapi import FastAPI
from fastapi import Depends

import csv

from backend.auth import verify_token

from sqlalchemy.orm import Session

from backend import crud
from backend import models
from backend import schemas

from backend.database import engine
from backend.database import SessionLocal

from fastapi.responses import FileResponse

from fastapi.security import OAuth2PasswordRequestForm

from backend.auth import verify_password
from backend.auth import create_access_token

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


@app.get("/")
def home():

    return {
        "message": "Employee Management API"
    }

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(
        models.User
    ).filter(
        models.User.username == form_data.username
    ).first()

    if not user:

        return {
            "message": "Invalid username"
        }

    stored_password = user.password

    if not verify_password(
        form_data.password,
        stored_password
    ):

        return {
            "message": "Invalid password"
        }

    access_token = create_access_token(
        data={
            "sub": form_data.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.post("/employees")
def add_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):

    return crud.create_employee(db, employee)


@app.get("/employees")
def view_employees(

    username: str = Depends(verify_token),

    db: Session = Depends(get_db)
):

    return crud.get_employees(db)

@app.get("/employees/sort")
def sort_employees(
    order: str = "asc",
    db: Session = Depends(get_db)
):

    employees = crud.sort_employees_by_salary(
        db,
        order
    )

    return employees

@app.get("/employees/export")
def export_csv(
    db: Session = Depends(get_db)
):

    employees = crud.export_employees_csv(db)

    file_path = "employees.csv"

    with open(
        file_path,
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Name",
            "Department",
            "Salary",
            "Email",
            "Created At"
        ])

        for employee in employees:

            writer.writerow([
                employee.id,
                employee.employee_name,
                employee.department,
                employee.salary,
                employee.email,
                employee.created_at
            ])

    return FileResponse(
        path=file_path,
        filename="employees.csv",
        media_type="text/csv"
    )

@app.get("/employees/{employee_id}")
def search_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = crud.get_employee_by_id(
        db,
        employee_id
    )

    if not employee:

        return {
            "message": "Employee not found"
        }

    return employee

@app.put("/employees/{employee_id}")
def update_salary(
    employee_id: int,
    new_salary: float,
    db: Session = Depends(get_db)
):

    employee = crud.update_employee_salary(
        db,
        employee_id,
        new_salary
    )

    if not employee:

        return {
            "message": "Employee not found"
        }

    return {
        "message": "Salary updated successfully",
        "employee": employee
    }

@app.delete("/employees/{employee_id}")
def remove_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = crud.delete_employee(
        db,
        employee_id
    )

    if not employee:

        return {
            "message": "Employee not found"
        }

    return {
        "message": "Employee deleted successfully"
    }

