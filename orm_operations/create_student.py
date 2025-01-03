@app.post("/students/")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, age=student.age, course=student.course)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
