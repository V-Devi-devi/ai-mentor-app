from fastapi import APIRouter, Depends

from app.schemas.chat import ChatRequest
from app.services.chat_service import generate_response
from app.core.dependencies import get_current_user

router = APIRouter()

@router.post("/message")
def chat(
    data: ChatRequest,
    current_user: str = Depends(get_current_user)
):

    response = generate_response(
        data.message
    )

    return {
        "user": current_user,
        "question": data.message,
        "answer": response
    }