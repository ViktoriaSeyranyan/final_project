@app.put("/update_student/{student_id}")
def update_student(student_id: int, new_name: str, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student and student.active:
        student.name = new_name
        db.commit()
        return {"message": "Student updated"}
    return {"message": "Student not found or inactive"}
