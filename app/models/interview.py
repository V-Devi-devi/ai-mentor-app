from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from datetime import datetime

from app.db.base import Base


class Interview(Base):
    __tablename__ = "interviews"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    role = Column(String)

    difficulty = Column(String)

    question = Column(String)

    answer = Column(String)

    score = Column(
        Integer,
        default=0
    )

    feedback = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )