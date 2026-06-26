from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from app.db.base import Base


class Roadmap(Base):
    __tablename__ = "roadmaps"

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

    level = Column(String)

    roadmap = Column(String)

    status = Column(
        String,
        default="pending"
    )