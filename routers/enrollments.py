from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Enrollment, Student, Course
from schemas import Enrollment as EnrollmentSchema
from typing import List, Union, Dict

enrollments_router = APIRouter()

@enrollments_router.post("/enrollments", response_model=EnrollmentSchema)
def create_enrollment(enrollment: EnrollmentSchema, db: Session = Depends(get_db)):
    """Create a new enrollment"""
    # Check if student and course exist
    db_student = db.query(Student).filter(Student.id == enrollment.student_id).first()
    db_course = db.query(Course).filter(Course.id == enrollment.course_id).first()
    
    if not db_student or not db_course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    
    db_enrollment = Enrollment(**enrollment.model_dump())
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment



@enrollments_router.get("/enrollments/student/{student_name}", response_model=Dict[str, Union[str, List[str]]])
def read_enrollments_by_student_name(student_name: str, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.name.ilike(f"%{student_name}%")).first()

    if not db_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    enrolled_courses = []
    for enrollment in db_student.enrollments:
        course = enrollment.course
        if course:
            enrolled_courses.append(course.name)

    if not enrolled_courses:
        raise HTTPException(status_code=404, detail=f"Student '{student_name}' has no enrollments.")

    return {"student": db_student.name, "courses": enrolled_courses}

@enrollments_router.get("/enrollments/course/{course_code}", response_model=Dict[str, Union[str, List[str]]])
def read_enrolled_students_by_course_code(course_code: str, db: Session = Depends(get_db)):
    """Returns the course name and a list of enrolled students' names."""
    db_course = db.query(Course).filter(Course.code == course_code).first()

    if not db_course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    enrolled_students = []
    for enrollment in db_course.enrollments:  # Iterate through the course enrollments
        student = enrollment.student  # Access the student directly through the relationship
        if student:  # Check if the student exists (may have been deleted)
            enrolled_students.append(student.name)

    if not enrolled_students:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No students enrolled in the course '{db_course.name}'.")

    return {"course": db_course.name, "students": enrolled_students}