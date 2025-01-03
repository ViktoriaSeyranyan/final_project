@app.get("/students/")
def read_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students
