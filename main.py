from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine

# Import Models
from app.models.user import User
from app.models.onboarding import Onboarding
from app.models.roadmap import Roadmap
from app.models.task import Task
from app.models.interview import Interview
from app.models.chat import Chat
from app.models.analytics import Analytics

# Import Routers
from app.api.auth import router as auth_router
from app.api.onboarding import router as onboarding_router
from app.api.chat import router as chat_router
from app.api.dashboard import router as dashboard_router
from app.api.roadmap import router as roadmap_router
from app.api.tasks import router as task_router
from app.api.interviews import router as interview_router
from app.api.analytics import router as analytics_router
from app.api.admin import router as admin_router

app = FastAPI(
    title="AI Mentor Backend",
    version="1.0.0"
)

# Create SQLite Tables
Base.metadata.create_all(bind=engine)

# Authentication
app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)

# Onboarding
app.include_router(
    onboarding_router,
    prefix="/api/onboarding",
    tags=["Onboarding"]
)

# AI Chat
app.include_router(
    chat_router,
    prefix="/api/chat",
    tags=["AI Chat"]
)

# Dashboard
app.include_router(
    dashboard_router,
    prefix="/api/dashboard",
    tags=["Dashboard"]
)

# Roadmap
app.include_router(
    roadmap_router,
    prefix="/api/roadmap",
    tags=["Roadmap"]
)

# Tasks
app.include_router(
    task_router,
    prefix="/api/tasks",
    tags=["Tasks"]
)

# Interviews
app.include_router(
    interview_router,
    prefix="/api/interviews",
    tags=["Interviews"]
)

# Analytics
app.include_router(
    analytics_router,
    prefix="/api/analytics",
    tags=["Analytics"]
)

# Admin
app.include_router(
    admin_router,
    prefix="/api/admin",
    tags=["Admin"]
)

@app.get("/")
def home():
    return {
        "message": "AI Mentor Backend Running"
    }