from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

DATABASE_URL = "sqlite:///./dekanat.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    fio = Column(String, index=True)
    birth_date = Column(String)
    city = Column(String)
    enrollment_year = Column(Integer)

class Faculty(Base):
    __tablename__ = 'faculties'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    dean = Column(String)
    seats = Column(Integer)

class Education(Base):
    __tablename__ = 'educations'
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    faculty_id = Column(Integer, ForeignKey('faculties.id'))
    group = Column(String)
    specialty = Column(String)
    stipend = Column(Float)
    year = Column(Integer)

Base.metadata.create_all(bind=engine)

class StudentCreate(BaseModel):
    fio: str
    birth_date: str
    city: str
    enrollment_year: int

class StudentUpdate(BaseModel):
    fio: str
    birth_date: str
    city: str
    enrollment_year: int

@app.post("/students/")
def create_student(student: StudentCreate):
    db = SessionLocal()
    try:
        new_student = Student(**student.dict())
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        logging.info(f"Добавлен студент: {new_student.fio}")
        return new_student
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@app.get("/students/")
def get_students(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    students = db.query(Student).offset(skip).limit(limit).all()
    db.close()
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    db.close()
    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")
    return student

@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
    db = SessionLocal()
    try:
        db_student = db.query(Student).filter(Student.id == student_id).first()
        if not db_student:
            raise HTTPException(status_code=404, detail="Студент не найден")
        for key, value in student.dict().items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
        logging.info(f"Обновлен студент ID: {student_id}")
        return db_student
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    db = SessionLocal()
    try:
        student = db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Студент не найден")
        db.delete(student)
        db.commit()
        logging.info(f"Удален студент ID: {student_id}")
        return {"message": "Студент удален"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@app.get("/students/search/")
def search_students(city: Optional[str] = None, year: Optional[int] = None):
    db = SessionLocal()
    query = db.query(Student)
    if city:
        query = query.filter(Student.city == city)
    if year:
        query = query.filter(Student.enrollment_year == year)
    results = query.all()
    db.close()
    return results
