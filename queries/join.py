@app.get("/students_with_faculty")
def get_students_with_faculty(db: Session = Depends(get_db)):
    query = db.query(Student, Faculty).join(Faculty, Student.faculty_id == Faculty.id)
    result = query.all()
    return [{"student": student.name, "faculty": faculty.name} for student, faculty in result]
