from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from app.predictor import predict_salary

app = FastAPI()

# Locate the existing frontend folder
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

# Serve CSS and JavaScript files
app.mount(
    "/static",
    StaticFiles(directory=str(FRONTEND_DIR)),
    name="static",
)


class Employee(BaseModel):
    age: int = Field(..., ge=18, le=65)
    experience: int = Field(..., ge=0, le=45)
    education: str
    department: str
    city: str
    previous_salary: int = Field(..., ge=0)


@app.get("/")
def home():
    return FileResponse(str(FRONTEND_DIR / "index.html"))


@app.post("/predict")
def predict_employee_salary(employee: Employee):
    salary = predict_salary(
        employee.age,
        employee.experience,
        employee.education,
        employee.department,
        employee.city,
        employee.previous_salary,
    )

    return {"predicted_salary": salary}