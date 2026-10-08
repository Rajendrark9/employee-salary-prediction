from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from app.predictor import predict_salary


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
    return {
        "message": "employees salary prediction api is running"
    }


@app.post("/predict")
def predict_employee_salary(employee: Employee):

    salary = predict_salary(
        employee.age,
        employee.experience,
        employee.education,
        employee.department,
        employee.city,
        employee.previous_salary
    )

    return {
        "predicted_salary": salary
    }