student = Student(
    name="John Doe",
    age=22,
    course="Math",
    extra_data={"bio": "John loves coding and open-source projects"}
)

db.add(student)
db.commit()
