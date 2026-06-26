from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from datetime import datetime

from app.db.base import Base


class Chat(Base):
    __tablename__ = "chats"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    # Groups messages into one conversation
    session_id = Column(
        String,
        index=True
    )

    # First question becomes chat title
    title = Column(
        String,
        default="New Chat"
    )

    question = Column(String)
    answer = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )