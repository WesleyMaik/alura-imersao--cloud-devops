from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Course
from schemas import Course as CourseSchema, Courses as CoursesSchema

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

# @cursos_router.get("/cursos/{curso_id}", response_model=Curso)
# def read_curso(curso_id: int, db: Session = Depends(get_db)):
#     db_curso = db.query(ModelCurso).filter(ModelCurso.id == curso_id).first()
#     if db_curso is None:
#         raise HTTPException(status_code=404, detail="Curso não encontrado")
#     return Curso.from_orm(db_curso)


# @cursos_router.delete("/cursos/{curso_id}", response_model=Curso)
# def delete_curso(curso_id: int, db: Session = Depends(get_db)):
#     db_curso = db.query(ModelCurso).filter(ModelCurso.id == curso_id).first()
#     if db_curso is None:
#         raise HTTPException(status_code=404, detail="Curso não encontrado")

#     curso_deletado = Curso.from_orm(db_curso)

#     db.delete(db_curso)
#     db.commit()
#     return curso_deletado