@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student:
        db_student.name = student.name
        db_student.age = student.age
        db_student.course = student.course
        db.commit()
        db.refresh(db_student)
    return db_student
