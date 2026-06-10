from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.onboarding import router as onboarding_router
from app.api.chat import router as chat_router

app = FastAPI(
    title="AI Mentor"
)

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

@app.get("/")
def home():
    return {
        "message": "Backend Running"
    }