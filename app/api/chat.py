from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.services.chat_service import generate_response

router = APIRouter()

@router.post("/message")
def chat(data: ChatRequest):

    response = generate_response(
        data.message
    )

    return {
        "question": data.message,
        "answer": response
    }