from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user

router = APIRouter()

@router.get("/")
def dashboard(
    current_user=Depends(get_current_user)
):
    return {
        "username": current_user,
        "message": "Welcome to AI Mentor Dashboard"
    }