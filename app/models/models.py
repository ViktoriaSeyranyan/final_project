from sqlalchemy import Column, Integer, String, Index
from app.db import Base  
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=True)  
    address = Column(String, nullable=True)  

    __table_args__ = (
        Index('ix_students_email', 'email'),
        Index('ix_students_address', 'address'),
    )