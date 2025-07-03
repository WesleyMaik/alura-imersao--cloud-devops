from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Enrollment, Student, Course
from schemas import Enrollment as EnrollmentSchema

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



@matriculas_router.get("/matriculas/aluno/{nome_aluno}", response_model=Dict[str, Union[str, List[str]]])
def read_matriculas_por_nome_aluno(nome_aluno: str, db: Session = Depends(get_db)):
    db_aluno = db.query(ModelAluno).filter(ModelAluno.nome.ilike(f"%{nome_aluno}%")).first()

    if not db_aluno:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    cursos_matriculados = []
    for matricula in db_aluno.matriculas:
        curso = matricula.curso  
        if curso:  
            cursos_matriculados.append(curso.nome)

    if not cursos_matriculados:
        raise HTTPException(status_code=404, detail=f"O aluno '{nome_aluno}' não possui matrículas cadastradas.")

    return {"aluno": db_aluno.nome, "cursos": cursos_matriculados}

@matriculas_router.get("/matriculas/curso/{codigo_curso}", response_model=Dict[str, Union[str, List[str]]])
def read_alunos_matriculados_por_codigo_curso(codigo_curso: str, db: Session = Depends(get_db)):
    """Returns the course name and a list of enrolled students' names."""
    db_curso = db.query(ModelCurso).filter(ModelCurso.codigo == codigo_curso).first()

    if not db_curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    alunos_matriculados = []
    for matricula in db_curso.matriculas:  # Iterate through the course enrollments
        aluno = matricula.aluno  # Access the student directly through the relationship
        if aluno:  # Check if the student exists (may have been deleted)
            alunos_matriculados.append(aluno.nome)

    if not alunos_matriculados:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No students enrolled in the course '{db_curso.nome}'.")

    return {"curso": db_curso.nome, "alunos": alunos_matriculados}