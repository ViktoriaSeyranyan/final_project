@app.get("/students")
def get_students(course: str = None, min_age: int = None, max_age: int = None, db: Session = Depends(get_db)):
    query = db.query(Student)
    if course:
        query = query.filter(Student.course == course)
    if min_age:
        query = query.filter(Student.age >= min_age)
    if max_age:
        query = query.filter(Student.age <= max_age)
    return query.all()
