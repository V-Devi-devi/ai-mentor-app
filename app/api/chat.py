import uuid

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.schemas.chat import ChatRequest
from app.services.chat_service import (
    generate_response
)

from app.core.dependencies import (
    get_current_user
)

from app.db.session import get_db

from app.models.chat import Chat
from app.models.user import User

router = APIRouter()


# ==========================
# Create New Chat Session
# ==========================
@router.post("/new")
def new_chat(
    current_user: User = Depends(
        get_current_user
    )
):
    return {
        "session_id": str(uuid.uuid4())
    }


# ==========================
# Send Message
# ==========================
@router.post("/message")
def chat(
    data: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    ai_response = generate_response(
        data.message
    )

    existing_chat = (
        db.query(Chat)
        .filter(
            Chat.session_id ==
            data.session_id
        )
        .first()
    )

    title = data.message

    if existing_chat:
        title = existing_chat.title

    new_chat_record = Chat(
        user_id=current_user.id,
        session_id=data.session_id,
        title=title,
        question=data.message,
        answer=ai_response
    )

    db.add(new_chat_record)
    db.commit()
    db.refresh(new_chat_record)

    return {
        "session_id": data.session_id,
        "question": data.message,
        "answer": ai_response
    }


# ==========================
# Get All Chat Sessions
# ==========================
@router.get("/history")
def get_chat_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    chats = (
        db.query(Chat)
        .filter(
            Chat.user_id ==
            current_user.id
        )
        .order_by(
            Chat.created_at.desc()
        )
        .all()
    )

    history = {}

    for chat in chats:

        if chat.session_id not in history:

            history[chat.session_id] = {
                "session_id": chat.session_id,
                "title": chat.title
            }

    return list(
        history.values()
    )


# ==========================
# Get One Conversation
# ==========================
@router.get(
    "/history/{session_id}"
)
def get_conversation(
    session_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    chats = (
        db.query(Chat)
        .filter(
            Chat.user_id ==
            current_user.id,
            Chat.session_id ==
            session_id
        )
        .order_by(
            Chat.created_at.asc()
        )
        .all()
    )

    if not chats:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    return [
        {
            "question": chat.question,
            "answer": chat.answer,
            "created_at": chat.created_at
        }
        for chat in chats
    ]