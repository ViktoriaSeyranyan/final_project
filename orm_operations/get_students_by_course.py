@app.get("/students/course/{course_name}")
def get_students_by_course(course_name: str, db: Session = Depends(get_db)):
    students = db.query(Student).filter(Student.course == course_name).all()
    return students
