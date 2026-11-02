
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from backend.database import get_db
from backend.models import Project
from backend.schemas import ProjectCreate, ProjectUpdate


app = FastAPI(
    title="AI Project Execution Intelligence Platform",
    description="API for tracking project progress and detecting delays",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "AI Project Intelligence API is running!",
        "status": "success"
    }
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Project Intelligence API"
    }
@app.get("/api/v1/project")
def get_project_info():
    return {
        "project_name": "AI Project Execution Intelligence Platform",
        "version": "1.0.0",
        "status": "in development",
        "features": [
            "Project progress tracking",
            "Schedule and report analysis",
            "Delay detection"
        ]
    }
@app.get("/api/v1/projects")
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return projects

@app.get("/api/v1/projects/{project_id}")
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project

@app.post("/api/v1/projects")
def create_project(project_data: ProjectCreate, db: Session = Depends(get_db)):
    new_project = Project(
        name=project_data.name,
        description=project_data.description,
        status=project_data.status
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project

@app.put("/api/v1/projects/{project_id}")
def update_project(
    project_id: int,
    project_data: ProjectUpdate,
    db: Session = Depends(get_db)
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    project.name = project_data.name
    project.description = project_data.description
    project.status = project_data.status

    db.commit()
    db.refresh(project)

    return project


