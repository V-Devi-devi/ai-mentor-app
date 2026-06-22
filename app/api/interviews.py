from fastapi import APIRouter, Depends
from app.services.interview_service import generate_questions
from app.core.dependencies import get_current_user

router = APIRouter()


@router.get("/questions")
def questions(
    role: str,
    difficulty: str,
    current_user: str = Depends(get_current_user)
):
    return {
        "user": current_user,
        "questions": generate_questions(
            role,
            difficulty
        )
    }