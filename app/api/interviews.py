from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.role_checker import role_required
from app.models.user import User

from app.services.interview_service import (
    generate_questions,
    evaluate_answer
)

from app.models.interview import Interview

router = APIRouter()


@router.get("/questions")
def questions(
    role: str,
    difficulty: str,
    current_user: User = Depends(
        role_required(["user", "admin"])
    )
):

    question = generate_questions(
        role,
        difficulty
    )

    return {
        "question": question
    }


@router.post("/answer")
def submit_answer(
    role: str,
    difficulty: str,
    question: str,
    answer: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        role_required(["user", "admin"])
    )
):

    result = evaluate_answer(
        question,
        answer
    )

    interview = Interview(
        user_id=current_user.id,
        role=role,
        difficulty=difficulty,
        question=question,
        answer=answer,
        score=result["score"],
        feedback=result["feedback"]
    )

    db.add(interview)
    db.commit()

    return {
        "score": result["score"],
        "feedback": result["feedback"]
    }