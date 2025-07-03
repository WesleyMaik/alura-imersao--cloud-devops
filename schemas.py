from pydantic import BaseModel, EmailStr
from typing import List

class Enrollment(BaseModel):
    student_id: int
    course_id: int

    class Config:
        from_attributes = True
        from_attributes = True

Enrollments = List[Enrollment]

class Student(BaseModel):
    name: str
    email: EmailStr
    phone: str

    class Config:
        from_attributes = True

Students = List[Student]

class Course(BaseModel):
    name: str
    code: str
    description: str

    class Config:
        from_attributes = True

Courses = List[Course]