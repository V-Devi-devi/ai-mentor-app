from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine

# Import models
from app.models.user import User
from app.models.roadmap import Roadmap

from app.api.auth import router as auth_router
from app.api.onboarding import router as onboarding_router
from app.api.chat import router as chat_router
from app.api.dashboard import router as dashboard_router
from app.api.roadmap import router as roadmap_router

app = FastAPI(
    title="AI Mentor"
)

# Create SQLite tables
Base.metadata.create_all(bind=engine)

app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)

app.include_router(
    onboarding_router,
    prefix="/api/onboarding",
    tags=["Onboarding"]
)

app.include_router(
    chat_router,
    prefix="/api/chat",
    tags=["AI Chat"]
)

app.include_router(
    dashboard_router,
    prefix="/api/dashboard",
    tags=["Dashboard"]
)

app.include_router(
    roadmap_router,
    prefix="/api/roadmap",
    tags=["Roadmap"]
)

@app.get("/")
def home():
    return {
        "message": "AI Mentor Backend Running"
    }