from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Student
from schemas import Student as StudentSchema, Students as StudentsSchema
from typing import List

students_router = APIRouter()

@students_router.get("/students", response_model=StudentsSchema)
def read_students(db: Session = Depends(get_db)):
    """Get all students"""
    return db.query(Student).all()

@students_router.get("/students/{student_id}", response_model=StudentSchema)
def read_student(student_id: int, db: Session = Depends(get_db)):
    """Get a student by ID"""
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@students_router.post("/students", response_model=StudentSchema)
def create_student(student: StudentSchema, db: Session = Depends(get_db)):
    """Create a new student"""
    db_student = Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@students_router.put("/students/{student_id}", response_model=StudentSchema)
def update_student(student_id: int, student: StudentSchema, db: Session = Depends(get_db)):
    """Update a student"""
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    for key, value in student.model_dump().items():
        setattr(db_student, key, value)
    
    db.commit()
    db.refresh(db_student)
    return db_student

@students_router.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    """Delete a student"""
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted successfully"}

@students_router.get("/students/name/{name}", response_model=StudentsSchema)
def read_student_by_name(name: str, db: Session = Depends(get_db)):
    """Get students by name"""
    db_students = db.query(Student).filter(Student.name.ilike(f"%{name}%")).all()
    if not db_students:
        raise HTTPException(status_code=404, detail="No student found with this name")
    return db_students

@students_router.get("/students/email/{email}", response_model=StudentSchema)
def read_student_by_email(email: str, db: Session = Depends(get_db)):
    """Get a student by email"""
    db_student = db.query(Student).filter(Student.email == email).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="No student found with this email")
    return db_student