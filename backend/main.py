
from fastapi import FastAPI

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
