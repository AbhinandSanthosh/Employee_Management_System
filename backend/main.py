from fastapi import FastAPI
from fastapi import Depends

import csv

import asyncio

import time

from backend.auth import (
    get_current_user,
    admin_only
)

from sentence_transformers import (
    SentenceTransformer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

from sqlalchemy.orm import Session

from fastapi import BackgroundTasks

from fastapi import WebSocket

from backend import crud
from backend import models
from backend import schemas

from backend.database import engine
from backend.database import SessionLocal

from fastapi.responses import FileResponse

from fastapi.security import OAuth2PasswordRequestForm

from backend.auth import verify_password
from backend.auth import create_access_token

from fastapi import UploadFile
from fastapi import File

from fastapi import BackgroundTasks
from PyPDF2 import PdfReader

models.Base.metadata.create_all(bind=engine)

SKILLS = [

    "Python",
    "FastAPI",
    "SQL",
    "PostgreSQL",
    "Docker",
    "AWS",
    "Machine Learning",
    "AI",
    "React",
    "JavaScript",
    "Git",
    "Linux"
]

resume_store = []

def send_welcome_email(
    employee_name: str
):

    import time

    print(
        f"Sending email to {employee_name}"
    )

    time.sleep(5)

    print(
        f"Welcome email sent to {employee_name}"
    )

def process_resume(

    file_path: str
):

    print(
        f"Processing resume: {file_path}"
    )

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        text += page.extract_text()

    print("Extracted Resume Text:")

    print(text[:500])

    skills = extract_skills(text)

    print("Detected Skills:")

    print(skills)

    embedding = generate_embedding(text)
    
    print("Embedding Vector Length:")
    
    print(len(embedding))

    embedding = generate_embedding(text)

    resume_store.append({
        
        "file": file_path,
        
        "text": text,
        
        "embedding": embedding,
        
        "skills": skills
    })

embedding_model = SentenceTransformer(

    "all-MiniLM-L6-v2"
)

def generate_embedding(

    text: str
):

    embedding = embedding_model.encode(text)

    return embedding

app = FastAPI()

@app.middleware("http")
async def log_requests(

    request,

    call_next
):

    start_time = time.time()

    print(
        f"Request: {request.method} {request.url}"
    )

    response = await call_next(request)

    process_time = (
        time.time() - start_time
    )

    print(
        f"Completed in {process_time:.4f} seconds"
    )

    return response

def get_db():

    db = SessionLocal()

    print("Database session created")

    try:

        yield db

    finally:

        print("Database session closed")

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

    background_tasks: BackgroundTasks,

    db: Session = Depends(get_db)
):

    result = crud.create_employee(
        db,
        employee
    )

    background_tasks.add_task(

        send_welcome_email,

        employee.employee_name
    )

    return result


@app.get("/employees")
def view_employees(

    username: str = Depends(get_current_user),

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

    current_user: str = Depends(admin_only),

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
    current_user: str = Depends(admin_only),
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

    current_user: str = Depends(admin_only),

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

@app.get("/async-test")
async def async_test():

    print("Request started")

    await asyncio.sleep(5)

    print("Request completed")

    return {
        "message": "Async route completed"
    }

@app.websocket("/ws")
async def websocket_endpoint(

    websocket: WebSocket
):

    await websocket.accept()

    while True:

        data = await websocket.receive_text()

        await websocket.send_text(

            f"Message received: {data}"
        )

@app.post("/upload-resume")
async def upload_resume(

    background_tasks: BackgroundTasks,

    file: UploadFile = File(...)
):
    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as f:

        content = await file.read()

        f.write(content)

    background_tasks.add_task(

        process_resume,

        file_location
    )


    return {
            "filename" : file.filename,

            "message" : "resume uploaded successfully"
        }

def extract_skills(text: str):

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in text.lower():

            found_skills.append(skill)

    return found_skills

def semantic_search(

    query: str
):

    query_embedding = generate_embedding(query)

    results = []

    print(type(query_embedding))
    
    print(resume_store)

    for resume in resume_store:

        similarity = cosine_similarity(

            [query_embedding],

            [resume["embedding"]]
        )[0][0]

        results.append({

            "file": resume["file"],

            "similarity": float(similarity),

            "skills": resume["skills"]
        })

    results.sort(

        key=lambda x: x["similarity"],

        reverse=True
    )

    print(resume_store)

    return results

@app.get("/semantic-search")
def semantic_search_api(

    query: str
):

    results = semantic_search(query)

    return results

