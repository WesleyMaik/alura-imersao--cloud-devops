from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Course
from schemas import Course as CourseSchema, Courses as CoursesSchema
from typing import List

courses_router = APIRouter()

@courses_router.get("/courses", response_model=CoursesSchema)
def read_courses(db: Session = Depends(get_db)):
    """Get all courses"""
    return db.query(Course).all()

@courses_router.post("/courses", response_model=CourseSchema)
def create_course(course: CourseSchema, db: Session = Depends(get_db)):
    """Create a new course"""
    db_course = Course(**course.model_dump())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@courses_router.put("/courses/{code}", response_model=CourseSchema)
def update_course(code: str, course: CourseSchema, db: Session = Depends(get_db)):
    """Update a course"""
    db_course = db.query(Course).filter(Course.code == code).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    
    for key, value in course.model_dump().items():
        setattr(db_course, key, value)
    
    db.commit()
    db.refresh(db_course)
    return db_course

@courses_router.get("/courses/code/{code}", response_model=CourseSchema)
def read_course_by_code(code: str, db: Session = Depends(get_db)):
    """Get a course by code"""
    db_course = db.query(Course).filter(Course.code == code).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="No course found with this code")
    return db_course


# Do not search for a course by ID or delete under any circumstances

# @courses_router.get("/courses/{course_id}", response_model=CourseSchema)
# def read_course(course_id: int, db: Session = Depends(get_db)):
#     db_course = db.query(Course).filter(Course.id == course_id).first()
#     if db_course is None:
#         raise HTTPException(status_code=404, detail="Course not found")
#     return db_course


# @courses_router.delete("/courses/{course_id}", response_model=CourseSchema)
# def delete_course(course_id: int, db: Session = Depends(get_db)):
#     db_course = db.query(Course).filter(Course.id == course_id).first()
#     if db_course is None:
#         raise HTTPException(status_code=404, detail="Course not found")

#     deleted_course = db_course

#     db.delete(db_course)
#     db.commit()
#     return deleted_course