from sqlalchemy.orm import Session

from backend import models
from backend import schemas

def create_employee(
    db: Session,
    employee: schemas.EmployeeCreate
):

    db_employee = models.Employee(

        employee_name=employee.employee_name,

        department=employee.department,

        salary=employee.salary,

        email=employee.email
    )

    db.add(db_employee)

    db.commit()

    db.refresh(db_employee)

    return db_employee


def get_employees(db: Session):

    return db.query(models.Employee).all()

def get_employee_by_id(
    db: Session,
    employee_id: int
):

    return db.query(
        models.Employee
    ).filter(
        models.Employee.id == employee_id
    ).first()

def update_employee_salary(
    db: Session,
    employee_id: int,
    new_salary: float
):

    employee = db.query(
        models.Employee
    ).filter(
        models.Employee.id == employee_id
    ).first()

    if not employee:

        return None

    employee.salary = new_salary

    db.commit()

    db.refresh(employee)

    return employee

def delete_employee(
    db: Session,
    employee_id: int
):

    employee = db.query(
        models.Employee
    ).filter(
        models.Employee.id == employee_id
    ).first()

    if not employee:

        return None

    db.delete(employee)

    db.commit()

    return employee

def sort_employees_by_salary(
    db: Session,
    order: str
):

    if order == "asc":

        return db.query(
            models.Employee
        ).order_by(
            models.Employee.salary.asc()
        ).all()

    else:

        return db.query(
            models.Employee
        ).order_by(
            models.Employee.salary.desc()
        ).all()
    
def export_employees_csv(
    db: Session
):

    return db.query(
        models.Employee
    ).all()