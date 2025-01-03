from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from models import Student
from database import get_db

app = FastAPI()

@app.get("/students/")
def get_students_paginated(db: Session = Depends(get_db), skip: int = Query(0, ge=0), limit: int = Query(10, le=100)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students
