from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "Hello world !"}

@app.get("/greet/{name}")
def greet(name:str):
    return {"messge" : f"Hello {name} "}

@app.get("/greetAge")
def greetwithage(name:str,age:Optional[int]=None):
    return {"message" : f"Hello {name} your age is {age}"}

class Student(BaseModel):
    name:str
    age:int
    rollNo:int

@app.post('/Create_Student')
def Create_Student(student:Student):
    return {
        "name":student.name,
        "age":student.age,
        "roll_no":student.rollNo
    }