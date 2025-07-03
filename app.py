from fastapi import FastAPI
from database import engine, Base
from routers.students import students_router
from routers.courses import courses_router
from routers.enrollments import enrollments_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gestão Escolar", 
    description="""
        Esta API fornece endpoints para gerenciar alunos, cursos e turmas, em uma instituição de ensino.  
        
        Permite realizar diferentes operações em cada uma dessas entidades.
    """, 
    version="1.0.0",
)

app.include_router(students_router, tags=["students"])
app.include_router(courses_router, tags=["courses"])
app.include_router(enrollments_router, tags=["enrollments"])