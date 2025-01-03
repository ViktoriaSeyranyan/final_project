@app.get("/students_count_by_faculty")
def students_count_by_faculty(db: Session = Depends(get_db)):
    result = db.query(Faculty.name, func.count(Student.id)).join(Student, Faculty.id == Student.faculty_id).group_by(Faculty.name).all()
    return [{"faculty": faculty, "student_count": count} for faculty, count in result]
