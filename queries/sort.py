@app.get("/students_sorted")
def get_students_sorted(sort_by: str = "name", db: Session = Depends(get_db)):
    if sort_by == "name":
        students = db.query(Student).order_by(Student.name).all()
    elif sort_by == "age":
        students = db.query(Student).order_by(Student.age).all()
    else:
        students = db.query(Student).all()
    return students
