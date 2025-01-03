from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from models import Student
from sqlalchemy import func
import re

app = FastAPI()

@app.get("/search")
def search_students(query: str, db: Session = Depends(get_db)):
    regex = f".*{query}.*"  
    results = db.query(Student).filter(
        func.jsonb_extract_path_text(Student.extra_data, 'field_name').op('~')(regex)
    ).all()
    return results
